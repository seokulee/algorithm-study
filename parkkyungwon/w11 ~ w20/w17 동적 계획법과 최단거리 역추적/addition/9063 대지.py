import sys



readline = sys.stdin.readline
N = int(readline())
arr = [i for i in zip(*[map(int, readline().split()) for _ in range(N)])]

x = max(arr[0]) - min(arr[0])
y = max(arr[1]) - min(arr[1])

print(x*y)
