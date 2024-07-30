def sol(n):
    ### e^x * sin(x) * cos(x)를 미분하면 e^x * sin(x) * cos(x) - e^x * sin^2(x) + e^x * cos^2(x)
    ### e^x * sin^2(x) 를 미분하면 2e^x * sin(x) * cos(x) + e^x * sin^2(x)
    ### e^x * cos^2(x) 를 미분하면 -2e^x * sin(x) * cos(x) + e^x * cos^2(x)
    a, b, c = 1, 0, 0
    for _ in range(n):
        a2 = a + 2*b - 2*c
        b2 = b - a
        c2 = c + a 

        a, b, c = a2, b2, c2

    return a + b + c

n = int(input())
print(sol(n))
