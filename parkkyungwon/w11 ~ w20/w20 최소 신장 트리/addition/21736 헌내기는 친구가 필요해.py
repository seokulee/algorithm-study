def sol(dp, length):
    start = dp.index(2)
    dp[start] = 0
    count = 0
    queue = [start]

    while queue:
        queue_tmp = []
        
        for q in queue:
            for i in q+1, q-1, q+length, q-length:
                if dp[i]:
                    if dp[i] == 3: count += 1

                    dp[i] = 0
                    queue_tmp.append(i)
        
        queue = queue_tmp

    return count if count else 'TT'


ss = open(0).read().splitlines()
N, M = map(lambda x: int(x) + 2, ss[0].split())

mapping = {'O': 1, 'X': 0, 'I': 2, 'P': 3}
maps = [0] * M
for s in ss[1:]:
    maps += [0] + list(map(lambda x: mapping[x], s)) + [0]
maps += [0] * M

print(sol(maps, M))
