import sys



def sol(arr):
    maxi = 0
    visited = [set() for _ in range(len(arr))]

    def dfs(i, mask, depth):
        nonlocal maxi

        if maxi < depth: maxi = depth
        if depth == 26: return True

        for j in i+1, i-1, i+L, i-L:
            if arr[j] < 0 or ((bit := 1 << arr[j]) & mask): continue

            new_mask = mask | bit

            if new_mask in visited[j]: continue 
            
            visited[j].add(new_mask)

            if dfs(j, new_mask, depth+1): return True

    dfs(L, 0, 0)
    
    return maxi


readline = sys.stdin.readline
R, C = map(int, readline().split())
L = C + 2
arr = [-1] * L
for _ in range(R):
    arr += [-1] + [ord(c) - 65 for c in readline().rstrip()] + [-1]
arr += [-1] * L

print(sol(arr))
