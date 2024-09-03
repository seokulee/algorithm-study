import sys



readline = sys.stdin.readline

c = int(readline())
nums = [int(readline()) for _ in range(c)]
dp = nums.copy()

for i in range(c-3):
    dp[i+3] = max(dp[i] + nums[i+1] + nums[i+3], dp[i+3])
    dp[i+2] = max(dp[i] + nums[i+2], dp[i+2])

if c > 2: dp[-1] = max(dp[-1], dp[-3] + nums[-1])
if c > 1: dp[-1] = max(dp[-1], dp[-2] + nums[-1])

sys.stdout.write(str(dp[-1]) + '\n')
