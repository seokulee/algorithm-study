import sys



def sol(n, m):
    L = n + 1
    dp = [False] * L

    def backtrack(arr, depth):
        if depth == m:
            write(' '.join(arr) + '\n')
            return

        for i in range(1, L):
            if dp[i]: continue

            dp[i] = True
            arr.append(str(i))
            backtrack(arr, depth+1)
            arr.pop()
            dp[i] = False

    backtrack([], 0)


write = sys.stdout.write
N, M = map(int, input().split())

sol(N, M)
