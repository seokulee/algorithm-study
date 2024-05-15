N = int(input())

a = [1 for _ in range(5)]
b = a.copy()
for _ in range(N-1):
    b[0] = a[1]
    b[1] = a[0] + a[2]
    b[2] = a[1] + a[3]
    b[3] = a[2] + a[4]
    b[4] = a[3] + a[4]

    a, b = b, a

print((a[0] + sum(a[1:]) * 2) % int(1e9))
