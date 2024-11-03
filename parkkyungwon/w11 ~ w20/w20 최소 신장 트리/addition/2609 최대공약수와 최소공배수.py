def get_gcd(a, b):
    while b:
        a %= b
        a, b = b, a
    
    return a


a, b = map(int, input().split())
gcd = get_gcd(a, b)
lcm = a * b // gcd

print(gcd, lcm, sep='\n')
