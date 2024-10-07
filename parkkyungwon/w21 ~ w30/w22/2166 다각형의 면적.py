import sys



readline = sys.stdin.readline
N = int(readline())

total = 0
px, py = map(int, readline().split())
lx, ly = px, py

for cx, cy in (map(int, readline().split()) for _ in range(N-1)):
    total += px*cy - cx*py
    px, py = cx, cy

total += px*ly - lx*py

print(round(abs(total) / 2 + 0.000000000000001, 1))
