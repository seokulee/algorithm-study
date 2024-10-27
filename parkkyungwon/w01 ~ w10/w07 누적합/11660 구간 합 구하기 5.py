import sys



readline = sys.stdin.readline

N, M = map(int, readline().split())

arr = [[0] * (N+1)]
for _ in range(N):
    arr.append([0] + list(map(int, readline().split())))

for y in range(N):
    for x in range(N):
        arr[y+1][x+1] = arr[y+1][x+1] + arr[y][x+1] + arr[y+1][x] - arr[y][x]

for _ in range(M):
    y1, x1, y2, x2 = map(int, readline().split())
    answer = arr[y1-1][x1-1] - arr[y2][x1-1] - arr[y1-1][x2] + arr[y2][x2]

    sys.stdout.write(str(answer) + '\n')
 