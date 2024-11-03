import sys
from itertools import cycle



readline = sys.stdin.readline

N, M, K = map(int, readline().split())

arr, x, y = [[0] * (M+1)], 'B', 'W'
for _ in range(N):
    arr.append([1] + [a == b for a, b in zip(readline().strip(), cycle((x, y)))])
    x, y = y, x

for y in range(N):
    for x in range(M):
        arr[y+1][x+1] += arr[y][x+1] + arr[y+1][x] - arr[y][x]

arr2 = []
for y in range(N-K+1):
    for x in range(M-K+1):
        arr2.append(arr[y][x] - arr[y+K][x] - arr[y][x+K] + arr[y+K][x+K])

result = min(min(arr2), (K ** 2) - max(arr2))

sys.stdout.write(str(result) + '\n')
