# base = (a - 2b)^2
# space = base * b
# space = b * (a - 2b)^2

# let
# f(x) = x^2
# g(x) = a - 2x
# d/dx * f(g(b))
# = 2(a - 2b) * (-2)
# = -4(a - 2b) 

# d/db space = (a - 2b)^2 -4b(a - 2b)
# = (a - 2b)(a - 2b - 4b)
# = (a - 2b)(a - 6b)
# b = a/2 or a/6
# if b = a/2, 부피는  0
# 따라서, b = a/6

n = int(input())
for _ in range(n):
    print(f'{float(input())/6:.10f}')
