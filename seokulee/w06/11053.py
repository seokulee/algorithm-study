import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = [1 for _ in range(N)]

for i in range(1, N):
    com = 0
    for j in range(i, -1, -1):
        if arr[i] > arr[j] > com:
            com = arr[j]
            result[i] = max(result[i], result[j] + 1)

print(max(result))
