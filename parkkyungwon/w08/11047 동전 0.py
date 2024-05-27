import sys



readline = sys.stdin.readline
N, K = map(int, readline().split())
arr = [int(readline()) for _ in range(N)]

count = 0
for i in range(N-1, -1, -1):
    count += K // arr[i]
    K %= arr[i]

    if K == 0:
        break

sys.stdout.write(str(count) + '\n')
