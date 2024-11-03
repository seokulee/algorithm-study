import sys



def sol(arr):
    visited = [[False] * M2 for _ in range(N2)]
    visited[1][1] = True
    for i in range(N2): visited[i][0], visited[i][-1] = True, True
    for j in range(M2): visited[0][j], visited[-1][j] = True, True

    queue = [(1, 1)]
    direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
    count = -1

    while queue:
        count += 1
        queue_tmp = []

        for x, y in queue:
            for dx, dy in direction:
                dx += x
                dy += y

                if visited[dy][dx]: continue

                if arr[dy][dx]:
                    arr[dy][dx] += 1
                
                    if arr[dy][dx] > 2: 
                        visited[dy][dx] = True
                        queue_tmp.append((dx, dy))

                else:
                    visited[dy][dx] = True
                    queue.append((dx, dy))
        
        queue = queue_tmp

    return count


readline = sys.stdin.readline
N, M = map(int, readline().split())
N2, M2 = N + 2, M + 2

arr = [[0] * M2]
for _ in range(N):
    arr += [[0] + list(map(int, readline().split())) + [0]]
arr += [[0] * M2]

print(sol(arr))