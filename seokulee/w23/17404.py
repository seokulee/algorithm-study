import sys

N = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
INF = int(1e9)
min_cost = INF

for j in range(3):
    result = [[INF] * 3 for _ in range(N)]
    result[0][j] = cost[0][j] 

    for i in range(1, N):
        result[i][0] = min(result[i - 1][1], result[i - 1][2]) + cost[i][0]
        result[i][1] = min(result[i - 1][0], result[i - 1][2]) + cost[i][1]
        result[i][2] = min(result[i - 1][0], result[i - 1][1]) + cost[i][2]

    for k in range(3):
        if j != k:
            min_cost = min(min_cost, result[N - 1][k])

print(min_cost)
# print(result)
