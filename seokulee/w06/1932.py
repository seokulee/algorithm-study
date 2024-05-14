import sys

N = int(sys.stdin.readline())
T = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = [[0] * i for i in range(1, N+1)]

for i in range(N):
    for j in range(i+1):
        if j == 0:
            result[i][j] = result[i-1][j] + T[i][j]
        elif j == i:
            result[i][j] = result[i-1][j-1] + T[i][j]
        else:
            result[i][j] = max(result[i-1][j-1], result[i-1][j]) + T[i][j]

print(max(result[-1]))
