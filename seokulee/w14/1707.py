import sys
sys.setrecursionlimit(10**6)

K = int(sys.stdin.readline().rstrip())

def dfs(x, color):
    visited[x] = color
    for y in graph[x]:
        if visited[y] == 0:
            if not dfs(y, -color):
                return False
        elif visited[y] == visited[x]:
            return False
    return True

for _ in range(K):
    V, E = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1):
        if visited[i] == 0:
            if not dfs(i, 1):
                print("NO")
                break
    else:
        print("YES")
