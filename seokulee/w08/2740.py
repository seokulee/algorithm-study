import sys

N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
_, K = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

result = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            result[i][j] += A[i][k] * B[k][j]

for i in range(N):
    print(*result[i])