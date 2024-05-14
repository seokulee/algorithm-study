import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

sum_arr = list()
sum_arr.append(0)

for i in range(N):
    sum_arr.append(arr[i] + sum_arr[-1])

result = list()

min_value = 0
idx = 0
for i in range(len(sum_arr)):
    if sum_arr[i] < min_value:
        if i == idx + 1:
            result.append(sum_arr[i] - sum_arr[i-1])
            min_value = sum_arr[i]
            idx = i
            continue
        result.append(max(sum_arr[idx:i]) - min(sum_arr[idx:i]))
        min_value = sum_arr[i]
        idx = i

if idx != N:
    result.append(max(sum_arr[idx:]) - min(sum_arr[idx:]))

print(max(result))