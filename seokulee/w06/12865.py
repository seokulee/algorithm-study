import sys


def solution():
    N, K = map(int, sys.stdin.readline().split())
    stuff = list()
    stuff.append((0, 0))

    for _ in range(N):
        W, V = map(int, sys.stdin.readline().split())
        stuff.append((W, V))

    pack = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if j >= stuff[i][0]:  # 현재 점수가 해당 가방 넣는 물건의 무게보다 많으면(자리있으면)
                pack[i][j] = max(stuff[i][1] + pack[i - 1][j - stuff[i][0]], pack[i - 1][j])
            else:
                pack[i][j] = pack[i - 1][j]

    return pack[N][K]


if __name__ == '__main__':
    print(solution())
