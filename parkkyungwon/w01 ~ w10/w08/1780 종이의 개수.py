import sys



def find(arr, N):
    def f(x, y, l):
        if l == 1:
            return (1, 0, 0) if arr[y][x] == -1 else (0, 1, 0) if arr[y][x] == 0 else (0, 0, 1)

        l2 = l // 3
        xs = (x, x+l2, x+2*l2)
        ys = (y, y+l2, y+2*l2)
        ar = tuple(f(a, b, l2) for b in ys for a in xs)

        if sum(ar[0]) == 1:
            for a in ar[1:]:
                if ar[0] != a:
                    break
            else:
                return ar[0]
        
        b = tuple(sum(v) for v in zip(*ar))

        return b

    return f(0, 0, N)
     

readline = sys.stdin.readline
N = int(readline())
arr = [tuple(map(int, readline().split())) for _ in range(N)]

for v in find(arr, N):
    sys.stdout.write(str(v) + '\n')
