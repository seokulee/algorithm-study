import sys



def o_dfs():
    global items, N
    comb = {}

    def dfs(i, w):
        if comb.get((i, w), 0):
            return comb[(i, w)]
        
        if N == i:
            return 0
        
        next = dfs(i+1, w)
        if w < items[i][0]:
            comb[(i, w)] = next
        else:
            comb[(i, w)] = max(dfs(i+1, w - items[i][0]) + items[i][1], next)
        
        return comb[(i, w)]
        
    return dfs(0, K)
        


readline = sys.stdin.readline

N, K = map(int, readline().split())
items = [tuple(map(int, readline().split())) for _ in range(N)]

sys.stdout.write(str(o_dfs()) + '\n')
