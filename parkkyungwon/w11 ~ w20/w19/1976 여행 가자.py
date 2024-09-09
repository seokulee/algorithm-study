import sys



def find(i):
    if dp[i] < 0: return i

    dp[i] = find(dp[i])

    return dp[i]


def union(a, b):
    if a == b: return

    ra, rb = find(a), find(b)
    if ra == rb: return
    
    if dp[ra] < dp[rb]: 
        dp[ra] += dp[rb]
        dp[rb] = ra
    else: 
        dp[rb] += dp[ra]
        dp[ra] = rb


readline = sys.stdin.readline
N = int(readline())
readline()
dp = [-1] * (N+1)

for i in range(1, N+1):
    arr = tuple(map(int, readline().split()))

    for j, a in enumerate(arr[i:], start=i+1):
        if a: union(i, j)

# 여행 계획에 중복된 도시는 제거
travel = set(map(int, readline().split()))

# 최상위 부모가 2개 이상이면 불가
answer = 'YES' if len(set(map(find, travel))) == 1 else 'NO'

print(answer)
