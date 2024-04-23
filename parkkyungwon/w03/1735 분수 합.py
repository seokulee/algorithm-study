def f_gcd(a, b):
    while(b):
        a, b = b, a % b
    
    return a

a, b = map(int, input().split())
c, d = map(int, input().split())

numerator = a*d + c*b
denominator  = b*d

while True:
    gcd = f_gcd(numerator, denominator)

    if gcd > 1:
        numerator //= gcd
        denominator //= gcd
    else:
        break

print(numerator, denominator)
