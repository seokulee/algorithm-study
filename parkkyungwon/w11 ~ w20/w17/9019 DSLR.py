import sys



L = 10000
# 각 수에서 다른 수로 변환(정방향, 역방향 모두)할 수 있는 수를 미리 전부 구함 
forward_path = [(i-1 if i else 9999, 10*i%L + i//1000, i//10 + 1000*i%L, 2*i%L) for i in range(L)]
backward_path = [(0 if i == 9999 else i+1, i//10 + 1000*i%L, 10*i%L + i//1000, j := i//2, j+5000)
            if i % 2 == 0 else 
            (0 if i == 9999 else i+1, i//10 + 1000*i%L, 10*i%L + i//1000) for i in range(L)]
forward_chars = ('S', 'L', 'R', 'D')
backward_chars = ('S', 'L', 'R', 'D', 'D')



# 출발 지점과 도착 지점 양쪽에서 동시에 dp를 계산해간다. 투 포인터, bfs
def sol(start, end):
    # 1번의 depth만 실행하고, 정방향과 역방향 dp가 겹치면 해당 인덱스 반환
    def bfs():
        queue_tmp = []

        for q in queue[0]:
            for next_q in path[0][q]:
                if dp[0][next_q] == None:
                    dp[0][next_q] = q

                    if dp[1][next_q]: return next_q

                    queue_tmp.append(next_q)

        queue[0] = queue_tmp
    
    # 정방향과 역방향 위치 변경
    def fb_swap():
        queue[0], queue[1] = queue[1], queue[0]
        dp[0], dp[1] = dp[1], dp[0]
        path[0], path[1] = path[1], path[0]

    # 겹치는 곳에서 최단 경로를 역추적
    def back_tracking(i):
        answer = []

        while dp[0][i] != i:
            for char, j in zip(chars[0], path[0][i]):
                if j == dp[0][i]:
                    answer.append(char)
                    i = j
                    break
        
        return answer

    dp = [[None] * L for _ in range(2)]
    dp[0][start] = start
    dp[1][end] = end
    queue = [[start], [end]]
    path = [forward_path, backward_path]

    # bfs가 끝나면 정방향과 역방향 위치 변경
    while 1:
        if (m := bfs()) != None: break
        fb_swap()

    # dp[0]이 정방향으로 설정
    if dp[0][start] != start: fb_swap() 

    # 최단 경로 추적
    path[0], path[1] = path[1], path[0]
    chars = [backward_chars, forward_chars]

    # 중앙에서 출발지
    answer = back_tracking(m)

    answer.reverse() 
    fb_swap()
    chars[0], chars[1] = chars[1], chars[0]

    # 중앙에서 도착지
    answer += back_tracking(m)
   
    return ''.join(answer)


readline = sys.stdin.readline
T = int(readline())

for _ in range(T):
    A, B = map(int, readline().split())

    sys.stdout.write(sol(A, B) + '\n')
