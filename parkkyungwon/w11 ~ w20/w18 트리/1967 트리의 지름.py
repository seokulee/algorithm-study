import sys



sys.setrecursionlimit(10**5)


def sol(edges):
    visited = [False] * (N+1)
    visited[1] = True
    maxi = 0

    def dfs(i):
        nonlocal maxi
        maxi2 = 0

        for j in edges[i]:
            if visited[j]: continue
            visited[j] = True

            child = dfs(j) + edges[i][j]
            a = child + maxi2

            # 자식 끼리의 거리가 글로벌 maximum 보다 크면 값 갱신
            if a > maxi: maxi = a
            # 자식 중 가장 큰 값을 로컬 maximum으로 반환
            if child > maxi2: maxi2 = child

        return maxi2
        
    dfs(1)

    return maxi


readline = sys.stdin.readline
N = int(readline())
edges = [{} for _ in range(N+1)]

for i, j, v in (map(int, readline().split()) for _ in range(N-1)):
    edges[i][j] = v
    edges[j][i] = v

print(sol(edges))
