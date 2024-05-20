import sys

N = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = [[0] * 3 for _ in range(N)]

for i in range(N):
    result[i][0] = min(result[i - 1][1], result[i - 1][2]) + cost[i][0]
    result[i][1] = min(result[i - 1][0], result[i - 1][2]) + cost[i][1]
    result[i][2] = min(result[i - 1][0], result[i - 1][1]) + cost[i][2]

print(min(result[N-1]))

# cost 만들고 대입하는 과정 없앰
