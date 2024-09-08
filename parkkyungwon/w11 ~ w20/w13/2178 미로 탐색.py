import sys


sys.setrecursionlimit(10**6)
readline = sys.stdin.readline


def connect(arr, n, m):
    spot = [set() for _ in range(n*m)]

    # 좌표를 계산하기 위해 coordin 변수 사용
    coordin = 0
    prev = 0
    determ = 2 ** (m-1)
    for curr in arr:
        # 2진수를 사용해서 연결된 정보를 저장
        # 위 아래가 1이면 연결됌
        v = prev & curr
        # 좌 우가 1이면 연결됌
        h = curr & (curr << 1)

        for i in range(m):
            if (v << i) & determ:
                spot[coordin].add(coordin - m)
                spot[coordin - m].add(coordin)
            
            if (h << i) & determ:
                spot[coordin].add(coordin + 1)
                spot[coordin + 1].add(coordin)

            coordin += 1
        
        prev = curr
    
    return spot
    

def bfs(spot, n, m):
    goal = n*m - 1
    hist = {0, }
    
    def f(curr_spot):
        # 다음 깊이의 spot들을 저장
        next_spot = []

        for i in curr_spot:
            for j in spot[i]:
                if j in hist:
                    continue

                if j == goal:
                    return 2

                next_spot.append(j)
                hist.add(j)
        
        return f(next_spot) + 1
    
    return f([0])


def sol(arr, n, m):
    # 입력을 2진수로 간주하고 정수로 저장
    arr2 = tuple(int(a, 2) for a in arr)
    # 각 정점마다, 다른 정점과 연결된 정보를 저장한다. 
    spot = connect(arr2, n, m)

    return bfs(spot, n, m)


N, M = map(int, readline().split())
arr = (readline() for _ in range(N))

print(sol(arr, N, M))
