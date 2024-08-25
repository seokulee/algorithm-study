import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

s, e = 0, N-1
answer = (arr[s], arr[e])

result = float('inf')
while s < e:
    sum_value = arr[s] + arr[e]

    if abs(sum_value) < abs(result):
        result = sum_value
        answer = (arr[s], arr[e])

    if sum_value > 0:
        e -= 1
    elif sum_value < 0:
        s += 1
    else:
        break

print(answer[0], answer[1])
