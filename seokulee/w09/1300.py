import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
s, e = 1, K

result = 0
while s < e:
    m = (s + e) // 2
    tmp = 0

    for i in range(1, N + 1):
        tmp += min(m // i, N)

    if tmp < K:
        s = m + 1
    else:
        e = m

print(e)
