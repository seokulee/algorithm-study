import sys



def sol(mat):
    mini = float('inf')
    height = len(mat)
    leng = len(mat[0])
    arr = [float('inf')] * leng

    def update(arr, i):
        return [a if a < b else b for a, b in zip(arr, mat[i])]

    def backtrack(arr, start, depth):
        nonlocal mini

        if depth == M: 
            v = sum(arr)
            if v < mini: mini = v
            return
        
        for i in range(start, height):
            backtrack(update(arr, i), i+1, depth+1)

    backtrack(arr, 0, 0)

    return mini


readline = sys.stdin.readline
N, M = map(int, readline().split())
homes, stores = [], []

for i in range(N):
    for j, v in enumerate(readline().split()):
        match v:
            case '1': homes.append((i, j))
            case '2': stores.append((i, j))

mat = [[abs(x1-x2) + abs(y1-y2) for x1, y1 in homes] for x2, y2 in stores]

print(sol(mat))
