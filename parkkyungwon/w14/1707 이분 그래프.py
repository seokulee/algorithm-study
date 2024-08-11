import sys



def sol(data, v):
    edges = tuple([] for _ in range(v+1))
    for d1, d2 in data:
        edges[d1].append(d2)
        edges[d2].append(d1)

    # 방문 기록을 위해 0은 방문한적이 없고
    # 1과 2를 사용해서 이웃인지 아닌지를 판단
    hist = [0] * (v+1)
    # 두 정점이 간선들을 통해서 연결되지 않을 수 있기 때문에, 모든 정점을 확인
    for i in range(1, v):
        if hist[i]:
            continue
        
        # 0은 depth의 끝으로 표시
        queue = [i, 0]
        hist[i] = 1
        a, b = 1, 2
        for q in queue:
            # depth의 끝이면
            if not q:
                # queue에 다른 정점이 추가되지 않았다면
                if not queue[-1]:
                    break

                queue.append(0)
                a, b = b, a
                continue

            for e in edges[q]:
                # 이웃 정점을 방문한 적이 없다면, 현재 정점의 숫자와 다른 숫자를 부여 (1 또는 2)
                if not hist[e]:
                    hist[e] = b
                    queue.append(e)
                
                # 이웃 정점을 방문했고 현재 정점과 숫자가 같으면 이분그래프가 아님
                elif hist[e] == a:
                    return 'NO'
            
    return 'YES'



readline = sys.stdin.readline
K = int(readline())
for _ in range(K):
    V, E = map(int, readline().split())
    data = (map(int, readline().split()) for _ in range(E))
    print(sol(data, V))
