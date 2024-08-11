import sys



def sol(arr, m):
    m += 2
    # 상자 테두리에 -1을 추가하고 상자를 1차원 배열로 저장
    box = [-1] * (m)
    for a in arr:
        box += [-1] + a + [-1]
    box += [-1] * (m)

    queue = []
    # 익은 토마토를 찾고 queue에 넣음
    for i in range(len(box)):
        if box[i] == 1:
            queue.append(i)
    # bfs depth의 끝을 구분하기 위해 -1을 만나면 해당 depth의 끝
    queue.append(-1)

    count = 0
    for a in queue:
        if a == -1:
            # queue내부에 -1 뒤로 다른것이 추가되지 않았다면 끝
            if queue[-1] == -1:
                break

            queue.append(-1)
            count += 1
            continue

        # 좌, 우, 상, 하 인덱스 확인
        for b in a-1, a+1, a+m, a-m:
            if box[b]:
                continue

            box[b] = 1
            queue.append(b)

    for a in box:
        # box에 0이 존재하면 -1
        if not a:
            return -1
        
    else:
        return count 


readline = sys.stdin.readline
M, N = map(int, readline().split())

arr = [list(map(int, readline().split())) for _ in range(N)]

print(sol(arr, M))
