import sys
# import math


N, K = map(int, sys.stdin.readline().split())
p = 1_000_000_007

def factorial(N):
    n = 1
    for i in range(2, N + 1):
        n = (n * i) % p
    return n

def po(base, top):
    if top == 0:
        return 1
    elif top % 2 == 0:
        return (po(base, top // 2) ** 2) % p
    else:
        return (po(base, top // 2) ** 2 * base) % p


print(((factorial(N) % p) * po((factorial(K) * factorial(N-K)) % p, (p-2)) % p))

# fact = [1] * (N+1)
# for i in range(1, N+1):
#     fact[i] = fact[i - 1] * i
#
# print(fact[N]//(fact[K]*fact[N-K]))

