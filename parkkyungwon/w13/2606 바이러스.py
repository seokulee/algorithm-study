import sys



readline = sys.stdin.readline


def sol(pairs, n):
    # 각 정점마다, 다른 정점과 연결된 정보를 저장한다. 
    spot = [set() for _ in range(n+1)]
    for a, b in pairs:
        spot[a].add(b)
        spot[b].add(a)

    # 그리고 연결된 정보를 오름차순으로 정렬한다.
    for i in range(len(spot)):
        spot[i] = sorted(spot[i])

    next_spot = [1]
    hist = {1, }
    
    # next_spot에 순차적으로 다음 탐색할 정점을 추가
    for i in next_spot:
        for j in spot[i]:
            if j in hist:
                continue

            next_spot.append(j)
            hist.add(j)
        
    return len(next_spot) - 1


N = int(readline())
M = int(readline())
pairs = (map(int, readline().split()) for _ in range(M))

print(sol(pairs, N))
