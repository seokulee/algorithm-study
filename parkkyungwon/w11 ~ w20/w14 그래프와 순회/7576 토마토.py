import sys



def sol(box, leng):
    # 익은 토마토를 찾고 queue에 넣음
    queue = [i for i in range(len(box)) if box[i] == 1]
    count = -1
            
    while queue:
        queue_tmp = []
        
        for q in queue:
            # 좌, 우, 상, 하 인덱스 확인
            for i in q-1, q+1, q+leng, q-leng:
                if box[i]: continue

                box[i] = 1
                queue_tmp.append(i)
        
        count += 1
        queue = queue_tmp

    # box에 0이 존재하면 -1
    return count if all(box) else -1


readline = sys.stdin.readline
M, N = map(int, readline().split())
L = M + 2

# 상자 테두리에 -1을 추가하고 상자를 1차원 배열로 저장
box = [-1] * L
for a in (list(map(int, readline().split())) for _ in range(N)):
    box += [-1] + a + [-1]
box += [-1] * L

print(sol(box, L))
