import sys

N = int(sys.stdin.readline().rstrip())
chu = list(map(int, sys.stdin.readline().rstrip().split()))
T = int(sys.stdin.readline().rstrip())
T_arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [[0 for _ in range(15001)] for _ in range(N + 1)]

def solve(n, w):
    if n > N or dp[n][w]:
        return

    dp[n][w] = 1

    solve(n+1, w+chu[n-1])
    solve(n+1, w)
    solve(n+1, abs(w-chu[n-1]))

solve(0, 0)

answer = list()
for t in T_arr:
    if t > 15000:
        answer.append('N')
    else:
        answer.append('Y') if dp[N][t] else answer.append('N')

print(*answer, sep=' ')
