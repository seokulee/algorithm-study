def egcd(a, b):
    c, d = 1, 0

    while b: 
        a, b, c ,d = b, a % b, d, c - (a // b * d)
    
    return a, c


N, A = map(int, input().split())

gcd, x = egcd(A, N)
mul_inv = x % N if gcd == 1 else -1

print(N-A, mul_inv)
