import sys




def find(arr, N):
    def f(x1, y1, x2, y2):
        if x2 - x1 == 1:
            return (0, 1) if arr[y1][x1] else (1, 0)

        xh, yh = (x1+x2)//2, (y1+y2)//2
        ar = (f(x1, y1, xh, yh), f(xh, y1, x2, yh), f(x1, yh, xh, y2), f(xh, yh, x2, y2))

        for a in ar:
            if a[0]:
                break
        else:
            return (0, 1)
        
        for a in ar:
            if a[1]:
                break
        else:
            return (1, 0)
        
        b = [0, 0]
        for a in ar:
            b[0] += a[0]
            b[1] += a[1]
        return b
    
    return f(0, 0, N, N)
     

readline = sys.stdin.readline
N = int(readline())
arr = [tuple(map(int, readline().split())) for _ in range(N)]

for v in find(arr, N):
    sys.stdout.write(str(v) + '\n')
