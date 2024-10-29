import sys
from heapq import heappop, heappush



def sol(arr):
    for y, a in enumerate(arr):
        if 9 in a:
            shark_coor = (y, a.index(9))
            a[shark_coor[1]] = 0
            break

    shark_up_count = 2
    shark_size = 2

    def bfs(y, x):
        nonlocal shark_size, shark_up_count

        queue = [(y, x)]
        visited = [[False] * L for _ in range(L)]
        visited[y][x] = True
        count = -1

        while queue:
            count += 1
            queue_tmp = []

            while queue:
                y, x = heappop(queue)

                if shark_size > arr[y][x] > 0:
                    shark_up_count -= 1
                    arr[y][x] = 0

                    if not shark_up_count:
                        shark_size += 1
                        shark_up_count = shark_size
                    
                    return y, x, count

                for dy, dx in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                    dx += x ; dy += y

                    if visited[dy][dx]: continue

                    visited[dy][dx] = True

                    if shark_size >= arr[dy][dx]: heappush(queue_tmp, (dy, dx))
    
            queue = queue_tmp

    time = 0

    while res := bfs(*shark_coor):
        shark_coor = res[:2]
        time += res[2]
    
    return time


readline = sys.stdin.readline
N = int(readline())
L = N + 2

wall = float('inf')
arr = [[wall] * L]
arr += [[wall] + list(map(int, readline().split())) + [wall] for _ in range(N)]
arr += [[wall] * L]

print(sol(arr))
