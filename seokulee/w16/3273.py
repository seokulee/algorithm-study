import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline().rstrip())

arr.sort()
s, e = 0, N - 1
count = 0

while s < e:
    result = arr[s] + arr[e]

    if result == target:
        count += 1
        s += 1
        e -= 1
    elif result > target:
        e -= 1
    else:
        s += 1

print(count)
