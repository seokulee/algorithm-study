import sys



def sol(data, n, m):
    if n == 1 and m == 1:
        return 1
    
    end_index = (n+1)*(m+2) - 2
    m += 2
    # 미로 테두리에 -1을 추가하고 미로를 1차원 배열로 저장
    maze = (-1,) * (m)
    for a in data:
        maze += (-1,) + a + (-1,)
    maze += (-1,) * (m)

    # maze의 방문 기록을 위해 hist변수 사용
    # 0는 방문 한 적 없고
    # 1은 벽을 한번 부수고 방문
    # 2은 벽을 부수지 않고 방문
    hist = [0] * len(maze)
    # bfs depth의 끝을 구분하기 위해 0을 만나면 해당 depth의 끝
    queue = [(2, m+1), (0, 0)]
    count = 1
    for n_break, index in queue:
        if not n_break:
            # queue내부에 -1 뒤로 다른것이 추가되지 않았다면 끝
            if not queue[-1][0]:
                break

            queue.append((0, 0))
            count += 1
            continue

        # 정답에 도달하면 끝
        elif index == end_index:
            return count

        # 좌, 우, 상, 하 인덱스 확인
        for a in index-1, index+1, index+m, index-m:
            # 1. 방문한 기록이 있으거나 끝 쪽이면 pass
            if n_break <= hist[a] or maze[a] == -1:
                continue

            # 1. 방문한 기록이 없고 끝 쪽이 아니고
            # 2. 벽으로 막혀있지 않다면 queue에 추가
            elif not maze[a]:
                hist[a] = n_break
                queue.append((n_break, a))

            # 1. 방문한 기록이 없고 끝 쪽이 아니고
            # 2. 벽으로 막혀있고
            # 3. 벽을 부순적이 없다면 queue에 추가
            elif n_break > 1:
                hist[a] = n_break - 1
                queue.append((n_break - 1, a))

    # 끝으로 도달하지 못해서 -1
    return -1


readline = sys.stdin.readline
N, M = map(int, readline().split())

data = (tuple(map(int, readline().strip())) for _ in range(N))

print(sol(data, N, M))
