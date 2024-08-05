import sys



sys.setrecursionlimit(10**6)
readline = sys.stdin.readline


def sol(input, n, v):
    # 각 정점마다, 다른 정점과 연결된 정보를 저장한다. 
    spot = [set() for _ in range(n+1)]
    for a, b in input:
        spot[a].add(b)
        spot[b].add(a)

    # 그리고 연결된 정보를 오름차순으로 정렬한다.
    for i in range(len(spot)):
        # 깊이 우선 탐색 1 코드에 정렬 방법만 변경
        spot[i] = sorted(spot[i], reverse=True)

    # 방문 기록을 저장하기 위해 list를  사용한다.
    hist = [0] * (n+1)
    count = 1

    def f(i):
        nonlocal count
        hist[i] = count
        count += 1

        for a in spot[i]:
            # 정점을 방문했었다면 패스
            if hist[a]:
                continue

            f(a)

    f(v)

    return hist[1:]


N, M, R = map(int, readline().split())
input = (map(int, readline().split()) for _ in range(M))

print(*sol(input, N, R), sep='\n')
