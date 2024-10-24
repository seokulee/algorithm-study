import sys



def sol(arr, n, m):
    dp = [False] * n
    answer = []

    def backtrack(depth):
        if depth == m:
            write(' '.join(answer) + '\n')
            return
        
        for i in range(n):
            if dp[i]: continue

            dp[i] = True
            answer.append(arr[i])
            backtrack(depth + 1)
            answer.pop()
            dp[i] = False

    backtrack(0)


write = sys.stdout.write
N, M = map(int, input().split())
arr = tuple(map(str, sorted(map(int, input().split()))))

sol(arr, N, M)
