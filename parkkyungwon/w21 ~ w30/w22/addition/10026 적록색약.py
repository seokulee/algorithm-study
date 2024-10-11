import sys



def rg_blind(a, b):
    return (a > 66) ^ (b > 66)


def no_rg_blind(a, b):
    return a != b


def sol(arr, func):
    dp = [0] * L*L
    dp[:L], dp[-L:] = [1] * L, [1] * L
    for i in range(L, L*L, L): 
        dp[i], dp[i+L-1] = 1, 1

    count = 0
    
    def bfs(start):
        queue = [start]
        det = arr[start]

        while queue:
            queue_tmp = []

            for q in queue:
                for i in q+1, q-1, q+L, q-L:
                    if dp[i] or func(arr[i], det): continue

                    dp[i] = 1
                    queue_tmp.append(i)
            
            queue = queue_tmp

    for i in range(L*L):
        if dp[i]: continue

        bfs(i)
        count += 1
    
    return count


readline = sys.stdin.readline
N = int(readline())
L = N + 2

arr = [0] * L
for _ in range(N):
    arr += [0] + list(map(ord, readline()[:-1])) + [0]
arr += [0] * L

print(sol(arr, no_rg_blind), sol(arr, rg_blind))
