import sys

N, K = map(int, sys.stdin.readline().split())
arr = list()

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

result = 0
while K:
    value = arr.pop()

    if K >= value:
        amount, K = divmod(K, value)
        result += amount

print(result)