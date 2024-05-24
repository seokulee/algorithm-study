def solve():
    global a

    a -= d
    if a > 0:
        return 0

    if a == 0:
        if b > 0:
            return 0
        
        if b == 0:
            return 0 if c > 0 else 1

        return 0 if -c/b > e else 1

    f = b**2 - 4*a*c
    if f <= 0:
        return 1
    
    g = (-b -f**(1/2)) / (2*a)
    return 0 if g > e else 1


a, b, c, d, e = map(int, open(0).read().split())

print(solve())
