import sys



readline = sys.stdin.readline


def sol(pairs, n, v):
    # 각 정점마다, 다른 정점과 연결된 정보를 저장한다. 
    spot = [set() for _ in range(n+1)]
    for a, b in pairs:
        spot[a].add(b)
        spot[b].add(a)

    # 그리고 연결된 정보를 오름차순으로 정렬한다.
    for i in range(len(spot)):
        spot[i] = sorted(spot[i])


    def dfs(a):
        dfs_hist_lst = [a]
        dfs_hist_set = {a, }
        
        def f(a):
            for b in spot[a]:
                # 정점을 방문했었다면 패스
                if b in dfs_hist_set:
                    continue

                dfs_hist_lst.append(b)
                dfs_hist_set.add(b)

                f(b)
        
        f(a)
        return dfs_hist_lst
        
        
    def bfs(a):
        bfs_hist_lst = [a]
        bfs_hist_set = {a, }
        
        # bfs_hist_lst에 순차적으로 다음 탐색할 정점을 추가
        for i in bfs_hist_lst:
            for j in spot[i]:
                if j in bfs_hist_set:
                    continue

                bfs_hist_lst.append(j)
                bfs_hist_set.add(j)
        
        return bfs_hist_lst

    
    return dfs(v), bfs(v)


N, M, V = map(int, readline().split())
pairs = (map(int, readline().split()) for _ in range(M))

for a in sol(pairs, N, V):
    print(*a)
