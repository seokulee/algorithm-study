import sys


def solution():
    N, M = map(int, sys.stdin.readline().split())
    arr = list()

    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))

    accum = [[0] * (N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            accum[i][j] = arr[i-1][j-1] + accum[i-1][j] + accum[i][j-1] - accum[i-1][j-1]

    for _ in range(M):
        a, b, c, d = map(int, sys.stdin.readline().split())

        num = accum[c][d] - accum[a-1][d] - accum[c][b-1] + accum[a-1][b-1]

        print(num)


if __name__ == '__main__':
    solution()
