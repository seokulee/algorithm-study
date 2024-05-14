import sys



readline = sys.stdin.readline


c = int(readline())
dp = [int(readline())]

for i in range(2, c+1):
    nums = list(map(int, readline().split()))

    nums[0] += dp[0]
    for j in range(1, i-1):
        nums[j] += max(dp[j-1], dp[j])
    nums[-1] += dp[-1]

    dp = nums

sys.stdout.write(str(max(dp)) + '\n')
