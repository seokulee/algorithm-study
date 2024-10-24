import sys



def sol(n, m):
    L = n + 1

    def backtrack(arr, depth):
        if depth == m:
            write(' '.join(arr) + '\n')
            return

        for j in range(1, L):
            arr.append(str(j))
            backtrack(arr, depth+1)
            arr.pop()

    backtrack([], 0)


write = sys.stdout.write
N, M = map(int, input().split())

sol(N, M)
