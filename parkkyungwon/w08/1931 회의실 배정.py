import sys



readline = sys.stdin.readline
N = int(readline())
arr = [tuple(map(int, readline().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))

d = 0
count = 0
for a in arr:
    if a[0] >= d:
        count += 1
        d = a[1]

sys.stdout.write(str(count) + '\n')
