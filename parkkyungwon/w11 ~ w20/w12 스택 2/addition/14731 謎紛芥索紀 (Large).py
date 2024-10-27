def sol(ck):
    next(ck)

    total = 0
    mod = int(10e8 + 7)
    for c, k in zip(ck, ck):
        total += c * k * pow(2, (k-1), mod)
        total %= mod
    
    return total


ck = map(int, open(0).read().split())

print(sol(ck))
