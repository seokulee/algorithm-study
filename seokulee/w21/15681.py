import sys
sys.setrecursionlimit(10 ** 6)

def dfs(tree, dp, root, prev_root):
    count = 1
    for node in tree[root]:
        if node == prev_root:
            continue
        count = count + (dp[node] if dp[node] != -1 else dfs(tree, dp, node, root))
    dp[root] = count

    return dp[root]


N, R, Q = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]


for _ in range(N - 1):
    U, V = map(int, sys.stdin.readline().split())
    graph[U].append(V)
    graph[V].append(U)


dp = [-1] * (N + 1)

dfs(graph, dp, R, None)

answer = []

for _ in range(Q):
    answer.append(dp[int(sys.stdin.readline())])

print(*answer, sep='\n')
