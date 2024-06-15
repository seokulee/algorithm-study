import sys



readline = sys.stdin.readline
tu = tuple


def power(arr, ex, M):
    arr = tu(tu(a % M for a in ar) for ar in arr)
    arr_T = tu(v for v in zip(*arr))
    
    def p(ex):
        if ex == 1:
            return arr
        
        A = p(ex//2)
        B = tu(v for v in zip(*A))
        C = tu(tu(sum(x*y for x, y in zip(a, b)) % M for b in B) for a in A)

        return C if ex % 2 == 0 else tu(tu(sum(x*y % M for x, y in zip(a, b)) % M for b in arr_T) for a in C)


    return p(ex)


N, B = map(int, readline().split())
arr = tu(tu(map(int, readline().split())) for _ in range(N))

for ar in power(arr, B, 1000):
    for a in ar:
        sys.stdout.write(str(a) + ' ')
    sys.stdout.write('\n')
