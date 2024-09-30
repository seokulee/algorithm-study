import sys



sys.setrecursionlimit(370000)


def sol(dp, length):
    start = dp.index(2)
    dp[start] = 0
    count = 0

    def dfs(i):
        nonlocal count

        for j in i+1, i-1, i+length, i-length:
            if dp[j]:
                if dp[j] == 3: count += 1

                dp[j] = 0
                dfs(j)

    dfs(start)

    return count if count else 'TT'


ss = open(0).read().splitlines()
N, M = map(lambda x: int(x) + 2, ss[0].split())

mapping = {'O': 1, 'X': 0, 'I': 2, 'P': 3}
maps = [0] * M
for s in ss[1:]:
    maps += [0] + list(map(lambda x: mapping[x], s)) + [0]
maps += [0] * M

print(sol(maps, M))
