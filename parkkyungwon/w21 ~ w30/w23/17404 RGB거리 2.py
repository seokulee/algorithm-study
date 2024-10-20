def sol(dp, data):
    # dp에서 인덱스 i와 다른 인덱스를 선택
    def compare(i):
        a, b = (dp[j] for j in range(3) if i != j)

        return [(a2 if a2 < b2 else b2) + rgb[i] for a2, b2 in zip(a, b)]
    
    for rgb in data:
        dp_tmp = [compare(i) for i in range(3)]
        dp = dp_tmp
    
    return min(*dp[0][1:3], dp[1][0], dp[1][2], *dp[2][0:2])


readline = open(0).readline
N = int(readline())
inf = float('inf')

a, b, c = map(int, readline().split())
dp = [[a, inf, inf],
      [inf, b, inf],
      [inf, inf, c],]

data = (tuple(map(int, readline().split())) for _ in range(N-1))

print(sol(dp, data))
