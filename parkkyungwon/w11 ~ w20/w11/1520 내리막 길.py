import sys



sys.setrecursionlimit(10**6)


def find(arr, V, H):
    dp = [[-1] * (H+2) for _ in range(V+2)]
    dp[-2][-2] = 1
    dp[1][1] = 0

    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def f(y, x):
        for dy, dx in directions:
            y2, x2 = y + dy, x + dx

            if arr[y][x] <= arr[y2][x2]: continue

            if dp[y2][x2] == -1:
                dp[y2][x2] = 0
                f(y2, x2)

            dp[y][x] += dp[y2][x2]

    f(1, 1)

    return dp[1][1]
    

readline = sys.stdin.readline
V, H = map(int, readline().split())

max_h = 10000

outline = [(max_h, ) * (H+2)]
arr = outline
for _ in range(V):
    arr += [[max_h, *(map(int, readline().split())), max_h]]
arr += outline

print(find(arr, V, H))
