import sys



def sol(arr, n, m):
    answer = []

    def backtrack(i, depth):
        if depth == m:
            write(' '.join(answer) + '\n')
            return
        
        prev = None
        
        for j in range(i, n):
            if arr[j] == prev: continue

            answer.append(arr[j])
            backtrack(j, depth + 1)
            answer.pop()

            prev = arr[j]

    backtrack(0, 0)


write = sys.stdout.write
N, M = map(int, input().split())
arr = tuple(map(str, sorted(map(int, input().split()))))

sol(arr, N, M)
