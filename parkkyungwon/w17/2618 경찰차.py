import sys



def sol(arr, n):
    L = len(arr)
    maxi = float('inf')
    diff = tuple([0] * (L+1) for _ in range(L+1))
    path = tuple([0] * (L+1) for _ in range(L+1))
    dp = tuple([float('inf')] * (L+1) for _ in range(L+1))
    dp[0][0] = 0

    # 두 사건간의 거리를 저장
    for i in range(L):
        diff[i+1][0] = sum(arr[i]) - 2
        diff[0][i+1] = 2*n - sum(arr[i])

        for j in range(i):
            a = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1])
            diff[i+1][j+1] = a
            diff[j+1][i+1] = a
    
    # 경우들 모두 계산
    for i in range(L):
        for j in range(L):
            if dp[i][j] >= maxi: continue

            if i < j: v = j + 1
            else: v = i + 1
            
            c1, c2 = diff[v][j] + dp[i][j], diff[i][v] + dp[i][j]

            if c1 < dp[i][v]: dp[i][v], path[i][v] = c1, j
            if c2 < dp[v][j]: dp[v][j], path[v][j] = c2, i
            
            if v == L:
                if c1 < maxi: maxi, answer = c1, (i, v)
                if c2 < maxi: maxi, answer = c2, (v, j)
                
    # 최단경로 역 추적
    nex = [answer[0], answer[1]]
    shor_path = []

    for i in range(L, 0, -1):
        if nex[0] == i:
            shor_path.append(2)
            nex[0] = path[nex[0]][nex[1]]
        else:
            shor_path.append(1)
            nex[1] = path[nex[0]][nex[1]]

    return dp[answer[0]][answer[1]], shor_path[::-1]


readline = sys.stdin.readline
N = int(readline())
W = int(readline())
arr = tuple(tuple(map(int, readline().split())) for _ in range(W))

answer, path = sol(arr, N)
print(answer, *path, sep='\n')
