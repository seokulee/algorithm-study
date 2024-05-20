import sys

T = int(sys.stdin.readline())
arr = [0] * 101
arr[1] = 1
arr[2] = 1
arr[3] = 1

for i in range(4, 101):
    arr[i] = arr[i - 2] + arr[i - 3]

for _ in range(T):
    N = int(sys.stdin.readline())

    print(arr[N])
