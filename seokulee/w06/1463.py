import sys

N = int(sys.stdin.readline())

result = [0] * (N + 1)

for i in range(1, N + 1):
    if i + 1 <= N:
        result[i + 1] = result[i] + 1 if result[i + 1] == 0 else min(result[i + 1], result[i] + 1)
    if i * 2 <= N:
        result[i * 2] = result[i] + 1 if result[i * 2] == 0 else min(result[i * 2], result[i] + 1)
    if i * 3 <= N:
        result[i * 3] = result[i] + 1 if result[i * 3] == 0 else min(result[i * 3], result[i] + 1)

print(result[N])
