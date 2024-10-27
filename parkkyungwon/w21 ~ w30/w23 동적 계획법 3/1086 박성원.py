import math
from fractions import Fraction



def sol(arr, q):
    # 기존 수열을 왼쪽으로 밀어내고 추가하는 수열을 오른쪽에 추가 
    # (j * 10^l + arr[i]) % q
    next_rs = [[] for _ in range(N)]
    for i in range(N):
        leng = 10 ** (len(str(arr[i])))
        next_rs[i] = [(j * (leng % q) + arr[i]) % q for j in range(q)]

    dp = [[0] * q for _ in range(1 << N)]
    dp[0][0] = 1

    for mask in range(1 << N):
        for i in range(N):
            bit = 1 << i 

            if mask & bit: continue

            for j in range(q):
                next_r = next_rs[i][j]
                dp[mask | bit][next_r] += dp[mask][j]

    return dp[-1][0]


arr = open(0).read().splitlines()
N = int(arr[0])
q = int(arr[-1])
arr = tuple(map(int, arr[1:-1]))

answer = Fraction(sol(arr, q), math.factorial(N))
match answer:
    case 1: answer = '1/1'
    case 0: answer = '0/1'

print(answer)
