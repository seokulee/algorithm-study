import sys



def inspect(start):
    # 간선이 n-1인지만 확인해도 트리인지 알 수 있다
    num_of_vertex = 0
    num_of_edge = 0
    visited[start] = True

    def dfs(i):
        nonlocal num_of_vertex, num_of_edge 
        
        num_of_vertex += 1
        num_of_edge += len(edges[i])

        for j in edges[i]:
            if visited[j]: continue

            visited[j] = True
            dfs(j)
    
    dfs(start)
    
    return True if num_of_edge//2 == num_of_vertex-1 else False


readline = sys.stdin.readline
case_num = 0

while 1:
    N, M = map(int, readline().split())

    if N == 0 and M == 0: break

    case_num += 1
    L = N + 1
    edges = [[] for _ in range(L)]

    for a, b in (map(int, readline().split()) for _ in range(M)):
        edges[a].append(b); edges[b].append(a)

    visited = [False] * L
    count = sum(inspect(i) for i in range(1, L) if not visited[i])
        
    if count == 0: answer = f'Case {case_num}: No trees.'
    elif count == 1: answer = f'Case {case_num}: There is one tree.'
    else: answer = f'Case {case_num}: A forest of {count} trees.'

    print(answer)
