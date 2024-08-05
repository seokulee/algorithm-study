import sys



readline = sys.stdin.readline


def sol(k, knight, goal):
    movements = ((-2, -1), (-1, -2), (2, -1), (1, -2), (2, 1), (1, 2), (-2, 1), (-1, 2))
    # 체스판에 방문했으면 1 아니면 0으로 기록한다.
    chess_board = [[0] * (k) for _ in range(k)]
    count = 0

    next_spot = [knight, (-1, -1)]
    chess_board[knight[1]][knight[0]] = 1

    for x, y in next_spot:
        if x == goal[0] and y == goal[1]:
            break
        
        # -1은 해당 depth의 끝을 알린다.
        elif x == -1:
            count += 1
            next_spot.append((-1, -1))
            continue
        
        for dx, dy in movements:
            dx += x
            dy += y
            # 체스판 범위를 벗어나면 무시한다.
            if dx >= k or dx < 0 or dy >= k or dy < 0 or chess_board[dy][dx]:
                continue

            chess_board[dy][dx] = 1
            next_spot.append((dx, dy))
    
    return count


N = int(readline())
for _ in range(N):
    K = int(readline())
    knight = tuple(map(int, readline().split()))
    goal = tuple(map(int, readline().split()))

    print(sol(K, knight, goal))
