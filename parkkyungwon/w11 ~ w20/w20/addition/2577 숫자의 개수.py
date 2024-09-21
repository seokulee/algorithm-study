a, b, c = (int(input()) for _ in range(3))
total = str(a * b * c)
dp = [0] * 10

for i in total: dp[int(i)] += 1

print('\n'.join(map(str, dp)))
