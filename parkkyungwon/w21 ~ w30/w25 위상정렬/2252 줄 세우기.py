import sys



def sol(dp, edges):
    answer = []
    queue = [i for i in range(1, L) if not dp[i]]

    while queue:
        queue_tmp = []
        
        for i in queue:
            for j in edges[i]:
                dp[j] -= 1

                if not dp[j]: queue_tmp.append(j)

            answer.append(i)

        queue = queue_tmp
    
    return answer


readline = sys.stdin.readline
N, M = map(int, readline().split())
L = N + 1

dp = [0] * L
edges = [[] for _ in range(L)]

for _ in range(M):
    a, b = map(int, readline().split())

    edges[a].append(b)
    dp[b] += 1

print(*sol(dp, edges))
