import sys

N = int(sys.stdin.readline())

arr = list()
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    arr.append((s, e))

arr.sort(key=lambda x: (x[1], x[0]))

end_time = -1
result = 0
for s, e in arr:
    if s >= end_time:
        end_time = e
        result += 1

print(result)