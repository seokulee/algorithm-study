import sys



L = 10000
# 각 수에서 다른 수로 변환(정방향, 역방향 모두)할 수 있는 수를 미리 전부 구해둠. 
forward_path = [(i-1 if i else 9999, 10*i%L + i//1000, i//10 + 1000*i%L, 2*i%L) for i in range(L)]
backward_path = [(0 if i == 9999 else i+1, i//10 + 1000*i%L, 10*i%L + i//1000, j := i//2, j+5000)
            if i % 2 == 0 else 
            (0 if i == 9999 else i+1, i//10 + 1000*i%L, 10*i%L + i//1000) for i in range(L)]
forward_chars = ('S', 'L', 'R', 'D')
backward_chars = ('S', 'L', 'R', 'D', 'D')


# 1번의 depth만 실행하고 다음 depth queue를 반환
def bfs(queue, path, dp):
    queue_tmp = []

    for q in queue:
        for next_q in path[q]:
            if dp[next_q] == None:
                dp[next_q] = q
                queue_tmp.append(next_q)
            
    return queue_tmp


# 충돌한 곳에서 최단 경로를 역추적
def back_tracking(i, dp, chars, path):
    answer = []

    while dp[i] != i:
        next_i = dp[i]
        for char, j in zip(chars, path[i]):
            if j == next_i:
                answer.append(char)
                i = j
                break
    
    return answer


# 충돌 확인
def is_collision(queue, dp):
    for i in queue: 
        if dp[i] != None: return i
    
    return -1


# 출발 지점과 도착 지점 양쪽에서 동시에 dp를 계산해간다. 투 포인터, bfs
def sol(start, end):
    forward_dp = [None] * L
    backward_dp = [None] * L
    forward_dp[start] = start
    backward_dp[end] = end
    forward_queue = [start]
    backward_queue = [end]

    while 1:
        forward_queue = bfs(forward_queue, forward_path, forward_dp)
        m = is_collision(forward_queue, backward_dp)
        if m != -1: break
        
        backward_queue = bfs(backward_queue, backward_path, backward_dp)
        m = is_collision(backward_queue, forward_dp)
        if m != -1: break

    # 최단 경로 추적
    answer = back_tracking(m, forward_dp, backward_chars, backward_path)
    answer.reverse() 
    answer += back_tracking(m, backward_dp, forward_chars, forward_path)
   
    return ''.join(answer)


readline = sys.stdin.readline
T = int(readline())

for _ in range(T):
    A, B = map(int, readline().split())

    sys.stdout.write(sol(A, B) + '\n')
