def forward(i):
    if (v := i-1) > -1: yield v
    if (v := i*2) < L: yield v
    if (v := i+1) < L: yield v


def sol():
    if N == K: return 0, 1
    if N > K: return N - K, 1

    case_dp = [0] * L
    case_dp[N] = 1
    visited = [False] * L
    visited[N] = True

    queue = [N]
    count = 0
    flag = True

    while flag:
        count += 1
        queue_tmp = []

        for q in queue:
            for i in forward(q):
                if visited[i]: continue
                if not case_dp[i]: queue_tmp.append(i)

                case_dp[i] += case_dp[q]

                if i == K: flag = False
            
        for q in queue:
            for i in forward(q):
                visited[i] = True

        queue = queue_tmp

    return count, case_dp[K]


N, K = map(int, input().split())
m = max(N, K)
L = m + 2

print(*sol(), sep='\n')
