import sys


def matmul(A, B):
    n = len(A)
    tmp = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            ele = 0
            for i in range(n):
                ele += A[row][i] * B[i][col]
            tmp[row][col] = ele % 1000000007

    return tmp


def matpo(A, K):
    if K == 1:
        return A

    half = matpo(A, K // 2)
    if K % 2 == 0:
        return matmul(half, half)
    else:
        return matmul(matmul(half, half), A)



N = int(sys.stdin.readline())
A = [[1, 1], [1, 0]]

result = matpo(A, N)
print(result[1][0] % 1000000007)
