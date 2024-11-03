n = int(input())

if n == 0:
    print(0)

else:
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, b + a

    print(b)
