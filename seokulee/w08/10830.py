import sys


# D for is odd
def matmul(A, B):
    n = len(A)
    tmp = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            ele = 0
            for i in range(n):
                ele += A[row][i] * B[i][col]
            tmp[row][col] = ele % 1000

    return tmp


def matpo(A, K):
    if K == 1:
        return A

    half = matpo(A, K // 2)
    if K % 2 == 0:
        return matmul(half, half)
    else:
        return matmul(matmul(half, half), A)


N, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
if K == 1:
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1000:
                A[i][j] = 0

result = matpo(A, K)
for r in result:
    print(*r)
