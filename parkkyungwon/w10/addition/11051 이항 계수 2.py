a, b = map(int, input().split())
b = min(b, a-b)
mod = 10007

af = 1
bf = 1
for i in range(a, a-b, -1): af = af * i % mod
for i in range(1, b+1): bf = bf * i % mod

c = 1
while bf * c % mod != 1: c += 1

print(af * c % mod)
