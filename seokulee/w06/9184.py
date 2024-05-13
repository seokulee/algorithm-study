import sys

Q = -1
memo = dict()

def w(a, b, c):
    if (a, b, c) in memo:
        return memo[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0:
        memo[(a, b, c)] = 1
        return 1

    elif a > 20 or b > 20 or c > 20:
        memo[(a, b, c)] = w(20, 20, 20)
        return w(20, 20, 20)

    elif a < b < c:
        result = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        memo[(a, b, c)] = result
        return result

    else:
        result = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        memo[(a, b, c)] = result
        return result



while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == Q and b == Q and c == Q:
        break

    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
