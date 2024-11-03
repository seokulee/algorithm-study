import sys



def sol(arr, edges, edges_rev):
    # bfs
    # w에 도달하는 정점만 식별
    visited_dp = [False] * L
    visited_dp[W] = True
    queue = [W]

    while queue:
        queue_tmp = []

        for q in queue:
            for e in edges_rev[q]:
                if visited_dp[e]: continue

                visited_dp[e] = True
                queue_tmp.append(e)
        
        queue = queue_tmp

    # w에 도달하는 것과 상관없는 간선 제거
    for i, visit in enumerate(visited_dp[1:], 1):
        if visit: edges[i] = [e for e in edges[i] if visited_dp[e]]
        else: del edges[i]

    # 위상 정렬
    cost_dp = [0] * L
    count_dp = [0] * L
    for key in edges: 
        for value in edges[key]:
            count_dp[value] += 1

    queue = [i for i, v in enumerate(count_dp[1:], 1) if not v and visited_dp[i]]

    while queue:
        queue_tmp = []

        for q in queue:
            for e in edges[q]:
                v = cost_dp[q] + arr[q]
                if v > cost_dp[e]: cost_dp[e] = v

                count_dp[e] -= 1
                if not count_dp[e]: queue_tmp.append(e)
        
        queue = queue_tmp
    
    return cost_dp[W] + arr[W]


readline = sys.stdin.readline
T = int(readline())

for _ in range(T):
    N, K = map(int, readline().split())
    L = N + 1

    arr = (0, ) + tuple(map(int, readline().split()))

    edges = {i: [] for i in range(1, L)}
    edges_rev = {i: [] for i in range(1, L)}
    for a, b in (map(int, readline().split()) for _ in range(K)):
        edges[a].append(b)
        edges_rev[b].append(a)

    W = int(readline())

    sys.stdout.write(str(sol(arr, edges, edges_rev)) + '\n')
