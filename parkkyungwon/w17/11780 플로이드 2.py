import sys



def floyd():
    for k in range(1, N):
        for i in range(1, N):
            for j in range(1, N):
                w = dp[i][k] + dp[k][j]
                if w < dp[i][j]:
                    dp[i][j] = w
                    # path[i][j]에 마지막으로 거처간 k를 저장
                    path[i][j] = k
    

def output():
    for i in range(1, N):
        yield map(lambda x: 0 if x == float('inf') else x, dp[i][1:])

    def f(i, j):
        k = path[i][j]
        if not k:
            return (j,)
        
        return f(i, k) + f(k, j)

    for i in range(1, N):
        for j in range(1, N):
            if i == j or path[i][j] == None:
                yield (0,)
            
            else:
                a = (i, ) + f(i, j)
                yield len(a), *a

    
readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline()) + 1
M = int(readline())

dp = tuple([float('inf')] * (N) for _ in range(N))
path = tuple([None] * N for _ in range(N))

for i in range(1, N):
    dp[i][i] = 0

for _ in range(M):
    i, j, w = map(int, readline().split())
    if w < dp[i][j]:
        dp[i][j] = w
        path[i][j] = 0

floyd()

for a in output():
    write(' '.join(map(str, a)) + '\n')
