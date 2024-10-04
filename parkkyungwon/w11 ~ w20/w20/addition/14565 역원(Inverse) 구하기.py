def inv(a, b):
    gcd = 0

    def f(a, b):
        nonlocal gcd

        if not b: 
            gcd = a
            return 1, 0
        
        x, y = f(b, a%b)

        return y, x - (a//b) * y

    x, y = f(a, b)

    return gcd, x, y


N, A = map(int, input().split())

mul_inv = i[2] % N if (i := inv(N, A))[0] == 1 else -1

print(N-A, mul_inv)
