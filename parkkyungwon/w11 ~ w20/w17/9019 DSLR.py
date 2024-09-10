import sys

readline = sys.stdin.readline
L = 10000
# 각 수에서 다른 수로 변환(정방향, 역방향 모두)할 수 있는 수를 미리 전부 구함 
fw_path = [(i-1 if i else 9999, 10*i%L + i//1000, i//10 + 1000*i%L, 2*i%L) for i in range(L)]
bw_path = [(0 if i == 9999 else i+1, i//10 + 1000*i%L, 10*i%L + i//1000, j := i//2, j+5000)
            if i % 2 == 0 else 
            (0 if i == 9999 else i+1, i//10 + 1000*i%L, 10*i%L + i//1000) for i in range(L)]
fw_chars = ('S', 'L', 'R', 'D')
bw_chars = ('S', 'L', 'R', 'D', 'D')

# 출발 지점과 도착 지점 양쪽에서 동시에 dp를 계산해간다. 투 포인터, bfs
def two_point_bfs(start, end):
    fw_dp = [-1] * L
    bw_dp = [-1] * L
    fw_dp[start] = start
    bw_dp[end] = end

    queue1, queue2 = [start], [end]
    dp1, dp2 = fw_dp, bw_dp
    path1, path2 = fw_path, bw_path

    while 1:
        tmp_queue = []

        for q in queue1:
            for next_q in path1[q]:
                if dp1[next_q] < 0:
                    dp1[next_q] = q
                    tmp_queue.append(next_q)
                
                    # 중간 지점을 찾으면 반환
                    if dp2[next_q] > -1: return next_q, fw_dp, bw_dp
        
        queue1, queue2 = queue2, tmp_queue
        dp1, dp2 = dp2, dp1
        path1, path2 = path2, path1

# 겹치는 곳에서 최단 경로를 역추적
def back_tracking(i, dp, chars, path):
    answer = []

    while dp[i] != i:
        for char, j in zip(chars, path[i]):
            if j == dp[i]:
                answer.append(char)
                i = j
                break
    
    return answer

def sol(start, end):
    m, fw_dp, bw_dp = two_point_bfs(start, end)
    # 최단 경로 추적
    answer = back_tracking(m, fw_dp, bw_chars, bw_path)
    answer.reverse() 
    answer += back_tracking(m, bw_dp, fw_chars, fw_path)
   
    return ''.join(answer)

def main():
    T = int(readline())

    for _ in range(T):
        A, B = map(int, readline().split())

        sys.stdout.write(sol(A, B) + '\n')


if __name__ == "__main__":
    main()