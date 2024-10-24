import sys



def sol(n, m):
    L = n + 1

    def backtrack(arr, i, depth):
        if depth == m:
            write(' '.join(arr) + '\n')
            return

        for j in range(i, L):
            arr.append(str(j))
            backtrack(arr, j, depth+1)
            arr.pop()

    backtrack([], 1, 0)


write = sys.stdout.write
N, M = map(int, input().split())

sol(N, M)
