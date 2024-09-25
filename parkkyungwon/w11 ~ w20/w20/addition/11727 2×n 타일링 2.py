# f(n) = f(n-1) + f(n-2)
def sol(n):
    a, b = 1, 1 # f(0), f(1)

    for _ in range(n):
        a, b = b, (2*a+b) % 10007

    return a


print(sol(int(input())))