import sys



readline = sys.stdin.readline
tu = tuple


def fibo(n, M):
    arr = ((1, 1), (1, 0))
    arr_T = tu(v for v in zip(*arr))
    
    def p(ex):
        if ex == 1:
            return arr
        
        A = p(ex//2)
        B = tu(v for v in zip(*A))
        C = tu(tu(sum(x*y for x, y in zip(a, b)) % M for b in B) for a in A)

        return C if ex % 2 == 0 else tu(tu(sum(x*y % M for x, y in zip(a, b)) % M for b in arr_T) for a in C)


    return p(n)


N = int(readline())

sys.stdout.write(str(fibo(N, 1000000007)[0][1]) + '\n')
