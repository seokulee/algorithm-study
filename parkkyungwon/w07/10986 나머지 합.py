import sys
from collections import defaultdict



readline = sys.stdin.readline

N, M = map(int, readline().split())
nums = list(map(int, readline().split()))

remainer_of_sums = [0] + nums
for i in range(N):
    remainer_of_sums[i+1] = (remainer_of_sums[i] + remainer_of_sums[i+1]) % M

num_of_remainer = defaultdict(int)
for remainer in remainer_of_sums:
    num_of_remainer[remainer] += 1

result = 0
for num in num_of_remainer:
    a = num_of_remainer[num]
    result += (a * (a-1)) // 2

sys.stdout.write(str(result) + '\n')
