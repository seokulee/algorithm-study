import sys
INF = int(1e9)

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

s = e = 0
sum_value = 0
answer = INF

while True:
    if sum_value >= S:
        answer = min(answer, e - s)
        sum_value -= arr[s]
        s += 1
    elif e == N:
        break
    else:
        sum_value += arr[e]
        e += 1

print(answer if answer != INF else 0)
