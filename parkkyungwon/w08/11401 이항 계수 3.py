def du(b, ex):
    def p(ex):
        if ex == 1:
            return b

        return ((p(ex//2) ** 2 % M) * (b if ex % 2 == 1 else 1)) % M

    return p(ex)
        

M = 1000000007
N, K = map(int, input().split())

K = K if N-K > K else N-K

a, b = 1, 1
for i in range(1, K+1):
    a = a * (N-i+1) % M
    b = b * i % M

print(a * du(b, M-2) % M)
