import sys



readline = sys.stdin.readline

c = int(readline())
dp = [list(map(int, readline().split())) for _ in range(c)]

for i in range(c-1):
    dp[i+1][0] += min(dp[i][1], dp[i][2])
    dp[i+1][1] += min(dp[i][0], dp[i][2])
    dp[i+1][2] += min(dp[i][0], dp[i][1])

sys.stdout.write(str(min(dp[-1])) + '\n')
