def sol(arr):
    visit = [[False] * M for _ in range(N)]
    di, dj = (-1, 0, 1, 0), (0, 1, 0, -1)
    max_val = max(map(max, arr))
    maxi = 0

    def dfs(i, j, depth, v):
        nonlocal maxi

        if v > maxi: maxi = v
        if depth == 3 or maxi >= v + max_val * (3 - depth): return

        for i2, j2 in zip(di, dj):
            i2 += i
            j2 += j
            
            if 0 <= i2 < N and 0 <= j2 < M and not visit[i2][j2]:
                visit[i2][j2] = True

                if depth == 1: dfs(i, j, depth + 1, v + arr[i2][j2])

                dfs(i2, j2, depth + 1, v + arr[i2][j2])

                visit[i2][j2] = False
        

    for i in range(N):
        for j in range(M):
            visit[i][j] = True
            dfs(i, j, 0, arr[i][j])
            visit[i][j] = False
    
    return maxi


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(sol(arr))
