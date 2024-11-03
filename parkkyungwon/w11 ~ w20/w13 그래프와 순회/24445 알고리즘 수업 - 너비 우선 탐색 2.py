import sys



readline = sys.stdin.readline


def sol(input, n, v):
    # 각 정점마다, 다른 정점과 연결된 정보를 저장한다. 
    spot = [set() for _ in range(n+1)]
    for a, b in input:
        spot[a].add(b)
        spot[b].add(a)

    # 그리고 연결된 정보를 내림차순으로 정렬한다.
    for i in range(len(spot)):
        spot[i] = sorted(spot[i], reverse=True)

    next_spot = [v]
    hist = [0] * (n+1)
    count = 1
    
    # next_spot에 순차적으로 다음 탐색할 정점을 추가
    for i in next_spot:
        hist[i] = count
        count += 1

        for j in spot[i]:
            if hist[j]:
                continue

            next_spot.append(j)
            # next_spot에 중복해서 들어갈 수 있기 때문에 임시로 1을 할당
            hist[j] = 1
        
    return hist[1:]


N, M, R = map(int, readline().split())
input = (map(int, readline().split()) for _ in range(M))

print(*sol(input, N, R), sep='\n')
