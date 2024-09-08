import sys


readline = sys.stdin.readline
N, M = map(int, readline().split())

dp = [-1] * (N+1)

def find(i):
    if dp[i] < 0: return i

    dp[i] = find(dp[i])

    return dp[i]

def union(a, b):
    if a == b: return

    ra, rb = find(a), find(b)
    if ra == rb: return
    
    # 집합의 크기가 작은 부모를 큰 부모로 가르켜야 계산양이 적다
    if dp[ra] < dp[rb]: 
        dp[ra] += dp[rb]
        dp[rb] = ra
    else: 
        dp[rb] += dp[ra]
        dp[ra] = rb

for _ in range(M):
    command, a, b = map(int, readline().split())

    if command:
        answer = 'yes' if find(a) == find(b) else 'no'
        sys.stdout.write(answer + '\n')
        
    else: union(a, b)
