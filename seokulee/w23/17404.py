import sys

N = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
INF = int(1e9)
min_cost = INF

# 첫 번째 집을 각각 다른 색으로 칠하는 경우를 따로 계산
for j in range(3):
    result = [[INF] * 3 for _ in range(N)]  # 각 케이스마다 초기화
    result[0][j] = cost[0][j]  # 첫 번째 집을 j번째 색으로 칠하는 경우

    for i in range(1, N):
        result[i][0] = min(result[i - 1][1], result[i - 1][2]) + cost[i][0]
        result[i][1] = min(result[i - 1][0], result[i - 1][2]) + cost[i][1]
        result[i][2] = min(result[i - 1][0], result[i - 1][1]) + cost[i][2]

    # 첫 번째 집과 마지막 집의 색이 같은 경우를 제외한 결과만 고려
    for k in range(3):
        if j != k:  # 첫 번째 집과 마지막 집의 색이 다른 경우만 최소값 계산
            min_cost = min(min_cost, result[N - 1][k])

print(min_cost)
# print(result)
