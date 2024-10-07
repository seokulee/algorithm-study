import sys



sys.setrecursionlimit(10**5)


def sol(weights, edges):
    dp = [[0, w] for w in weights]
    route = []

    # 자식에서 부모로 전달
    def weight_dfs(parent, cur):
        for chi in edges[cur]:
            if chi == parent: continue

            weight_dfs(cur, chi)

            dp[cur][0] += dp[chi][0] if dp[chi][0] > dp[chi][1] else dp[chi][1]
            dp[cur][1] += dp[chi][0]
        
    # 부노 노드가 선택된 상태를 stat에 저장
    def route_dfs(parent, cur, stat):
        if not stat and dp[cur][0] < dp[cur][1]:
            stat = True
            route.append(cur)

        else:
            stat = False

        for chi in edges[cur]:
            if chi == parent: continue

            route_dfs(cur, chi, stat)


    weight_dfs(0, 1)
    route_dfs(0, 1, False)

    return max(dp[1]), sorted(route)


readline = sys.stdin.readline
N = int(readline())

weights = [0] + list(map(int, readline().split()))

edges = [[] for _ in range(N+1)]
for a, b in (map(int, readline().split()) for _ in range(N-1)):
    edges[a].append(b)
    edges[b].append(a)

dp, route = sol(weights, edges)

print(dp)
print(*route)
