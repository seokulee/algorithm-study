import sys
from itertools import accumulate

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    K = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    cumsum = [0] + (list(accumulate(arr)))
    dp = [[0 for _ in range(K)] for _ in range(K)]

    for i in range(1, K):
        for j in range(K-i):
            x = j
            y = i+j
            dp[x][y] = float('inf')
            for k in range(x, y):
                dp[x][y] = min(dp[x][y], dp[x][k]+dp[k+1][y])
            dp[x][y] += cumsum[y+1]-cumsum[x]

    print(dp[0][K-1])
