import sys

N = int(sys.stdin.readline())

result = [[0] * 10 for _ in range(N)]
result[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, N):
    result[i][0] = result[i - 1][1]
    result[i][9] = result[i - 1][8]

    for j in range(1, 9):
        result[i][j] = result[i-1][j-1] + result[i-1][j+1]

print(sum(result[N-1]) % 1000000000)
