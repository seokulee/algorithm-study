import sys


def sameColor(N, paper, cnt):
    if sum(map(sum, paper)) == 0:
        cnt[0] += 1
        return
    elif sum(map(sum, paper)) == N ** 2:
        cnt[1] += 1
        return

    sameColor(N // 2, [row[:N // 2] for row in paper[:N // 2]], cnt)
    sameColor(N // 2, [row[N // 2:] for row in paper[:N // 2]], cnt)
    sameColor(N // 2, [row[:N // 2] for row in paper[N // 2:]], cnt)
    sameColor(N // 2, [row[N // 2:] for row in paper[N // 2:]], cnt)


N = int(sys.stdin.readline().strip())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 0: w, 1: b
cnt = [0] * 2

sameColor(N, paper, cnt)

print(cnt[0])
print(cnt[1])
