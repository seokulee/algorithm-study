import sys



def sol(a, b, n):
    if n > 1:
        b[1] += a[0]
        a[1] += b[0]

        for i in range(2, n):
            a[i] += b[i-1] if b[i-1] > b[i-2] else b[i-2]
            b[i] += a[i-1] if a[i-1] > a[i-2] else a[i-2]

    return a[-1] if a[-1] > b[-1] else b[-1]


readline = sys.stdin.readline
T = int(readline())

for _ in range(T):
    n = int(readline())
    a = list(map(int, readline().split()))
    b = list(map(int, readline().split()))

    sys.stdout.write(str(sol(a, b, n)) + '\n')
