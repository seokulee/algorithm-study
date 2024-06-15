import sys



def find(arr, N):
    def f(x1, y1, x2, y2):
        if x2 - x1 == 1:
            return 1 if arr[y1][x1] else 0

        xh, yh = (x1+x2)//2, (y1+y2)//2
        ar = (f(x1, y1, xh, yh), f(xh, y1, x2, yh), f(x1, yh, xh, y2), f(xh, yh, x2, y2))

        a = ar[0]
        for b in ar[1:]:
            if not(a is b):
                break
        else:
            return a
        
        return ar

    r = f(0, 0, N, N)
    r = str(r).replace(' ', '').replace(',', '')

    return r

readline = sys.stdin.readline
N = int(readline())
arr = [tuple(map(int, readline().strip())) for _ in range(N)]

sys.stdout.write(find(arr, N) + '\n')
