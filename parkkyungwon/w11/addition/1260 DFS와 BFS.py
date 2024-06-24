import sys



def dfs(arr, V):
    hist_set = set()
    hist_list = []

    hist_set.add(V)
    hist_list.append(V)

    def f(i):
        for a in arr[i]:
            if a in hist_set:
                continue

            hist_set.add(a)
            hist_list.append(a)
            f(a)

    f(V)

    return hist_list

    
def bfs(arr, V):
    hist_set = set()
    hist_list = []

    hist_set.add(V)
    hist_list.append(V)

    def f(i):
        for a in arr[i]:
            if a in hist_set:
                continue

            hist_set.add(a)
            hist_list.append(a)
        
    for h in hist_list:
        f(h)

    return hist_list


readline = sys.stdin.readline
N, M, V = map(int, readline().split())
arr = [set() for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, readline().split())
    arr[a].add(b)
    arr[b].add(a)

for i in range(len(arr)):
    arr[i] = sorted(arr[i])

print(*dfs(arr, V))
print(*bfs(arr, V))
