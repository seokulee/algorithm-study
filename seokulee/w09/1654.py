import sys

N, K = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]

l, r = 1, max(arr)
while l <= r:
    m = (l + r) // 2

    lines = 0
    for i in arr:
        lines += i // m

    if lines >= K:
        l = m + 1
    else:
        r = m - 1

print(r)
