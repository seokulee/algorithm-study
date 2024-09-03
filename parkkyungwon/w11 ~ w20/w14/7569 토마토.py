import sys



def sol(arr, m, n, h):
    m += 2
    area = m * (n + 2)

    # 상자 테두리에 -1을 추가하고 상자를 1차원 배열로 저장
    box = [-1] * (area)
    for _ in range(h):
        box += [-1] * (m)
        for _ in range(n):
            box += [-1] + next(arr) + [-1]
        box += [-1] * (m)
    box += [-1] * (area)

    queue = []
    zero_count = 0
    # 익은 토마토는 queue에, 익지 않은 토마토는 개수를 계산
    for i in range(len(box)):
        if box[i] == 1:
            queue.append(i)
        
        elif not box[i]:
            zero_count += 1

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

        # 좌, 우, 전, 후, 상, 하 인덱스 확인
        for b in a-1, a+1, a+m, a-m, a+area, a-area:
            if box[b]:
                continue

            box[b] = 1
            queue.append(b)
            zero_count -= 1

    # 익지 않은 토마토 개수를 구해서 정답 개수를 결정
    if zero_count:
        return -1
    else:
        return count


readline = sys.stdin.readline
M, N, H = map(int, readline().split())

arr = (list(map(int, readline().split())) for _ in range(N * H))

print(sol(arr, M, N, H))
