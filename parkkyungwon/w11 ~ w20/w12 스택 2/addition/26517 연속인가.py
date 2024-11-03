k = int(input())
a, b, c, d = map(int, input().split())

u = a * k + b
v = c * k + d

if u == v:
    print('Yes', u)

else:
    print('No')
