import sys



def sol(dp, n, leng):
    start = arr.index(2)
    dp[start] = 0
    queue = [start]
    dist = [0] * n * leng 

    while queue:
        tmp_queue = []

        for q in queue:
            w = dist[q] + 1

            for i in q+1, q-1, q+leng, q-leng:
                if not dp[i]: continue

                dp[i] = 0
                dist[i] = w
                tmp_queue.append(i)

        queue = tmp_queue

    for i in range(n * leng):
        if dp[i]: dist[i] = -1

    return dist


ss = sys.stdin.read().splitlines()
N, M = map(int, ss[0].split())
L = M + 2

arr = [0] * (L)
for s in ss[1:]:
    arr += [0] + list(map(int, s.split())) + [0]
arr += [0] * (L)

dist = sol(arr, N+2, L)
dist = [dist[i:i+L-2] for i in range(L+1, (N+1)*L, L)]

sys.stdout.writelines(' '.join(map(str, s)) + '\n' for s in dist)
