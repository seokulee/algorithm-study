import sys



def find(i):
    if dp[i] < 0: return i

    dp[i] = find(dp[i])

    return dp[i]


def union(a, b):
    if a == b: return

    ra, rb = find(a), find(b)
    if ra == rb: return True
    
    if dp[ra] < dp[rb]: 
        dp[ra] += dp[rb]
        dp[rb] = ra
    else: 
        dp[rb] += dp[ra]
        dp[ra] = rb


readline = sys.stdin.readline
N, M = map(int, readline().split())
dp = [-1] * (N)
answer = 0

for i in range(1, M+1):
    a, b = tuple(map(int, readline().split()))

    if union(a, b): 
        answer = i
        break

print(answer)
