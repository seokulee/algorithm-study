import sys



readline = sys.stdin.readline


def connection(arr, m, n):
    # 배열을 x축을 기준으로, 2진수로 변경 한다
    binary = [sum(a * (2 ** b) for a, b in zip(arr[i], range(m))) for i in range(n)]
    spot = [set() for _ in range(m*n)]

    # 좌표를 계산하기 위해 coordin 변수 사용
    # 가장 위, 오른쪽을 0으로 시작하고 왼쪽으로 1칸씩 좌표값이 1 증가.
    coordin = 0
    prev = 0
    for curr in binary:
        # 2진수를 사용해서 연결된 정보를 저장
        # 위 아래가 1이면 연결됌
        v = prev & curr
        for i in range(m):
            if (v >> i) & 1:
                spot[coordin].add(coordin - m)
                spot[coordin - m].add(coordin)
            
            coordin += 1
        
        prev = curr
    
    coordin = 0
    for curr in binary:
        # 좌 우가 1이면 연결됌
        h = curr & (curr >> 1)
        for i in range(m):
            if (h >> i) & 1:
                spot[coordin].add(coordin + 1)
                spot[coordin + 1].add(coordin)
            
            coordin += 1
    
    return spot


def sol(arr, m, n, k):
    # 입력을 m*n 배열에 표시한다.
    mapping = [[0] * m for _ in range(n)]
    for x, y in arr:
        mapping[y][x] = 1

    # 각 정점마다, 다른 정점과 연결된 정보를 저장한다. 
    spot = connection(mapping, m, n)


    def bfs(a):
        hist_lst = [a]
        hist_set = {a, }
        
        # hist_lst에 순차적으로 다음 탐색할 정점을 추가
        for i in hist_lst:
            for j in spot[i]:
                if j in hist_set:
                    continue

                hist_lst.append(j)
                hist_set.add(j)
            
            # 방문했던 정점의 연결 정보 제거
            spot[i] = set()
            
        return len(hist_lst)
            

    count = k
    for i in range(m*n):
        if spot[i]:
            # 총 배추 개수에서 인접한 배추 끼리 묶여지는 그룹의 크기만큼 뺀다. 
            # 그리고 그 그룹에 지렁이 1개가 필요함으로 1을 더한다.
            count += 1 - bfs(i)
    
    return count


T = int(readline())
for _ in range(T):
    M, N, K = map(int, readline().split())
    arr = (map(int, readline().split()) for _ in range(K))
    print(sol(arr, M, N, K))
