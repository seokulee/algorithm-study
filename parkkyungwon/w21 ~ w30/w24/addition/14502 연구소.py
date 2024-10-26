def sol(arr):
    virus = [i for i, a in enumerate(arr) if a == 2]
    num_init_virus = len(virus)
    leng = len(arr)
    width = M + 2
    min_count = float('inf')

    def check(dp):
        nonlocal min_count
        queue = virus
        count = num_init_virus

        while queue:
            queue_tmp = []

            for q in queue:
                for i in q+1, q-1, q+width, q-width:
                    if dp[i]: continue

                    dp[i] = 2
                    queue_tmp.append(i)
                    count += 1

                    if count >= min_count: return

            queue = queue_tmp
        
        min_count = count

    def bfs(i, depth):
        if depth == 3: 
            check(arr.copy())
            return

        for j in range(i, leng):
            if arr[j]: continue

            arr[j] = 1
            bfs(j+1, depth+1)
            arr[j] = 0
    
    bfs(0, 0)
    
    return arr.count(0) - (min_count - num_init_virus) - 3


ss = open(0).read().splitlines()
N, M = map(int, ss[0].split())

arr = [1] * (M+2)
for s in ss[1:]:
    arr += [1] + list(map(int, s.split())) + [1]
arr += [1] * (M+2)

print(sol(arr))