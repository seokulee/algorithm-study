import sys


def sameNumber(N, paper, cnt):
    if max(map(max, paper)) == min(map(min, paper)) == 0:
        cnt[1] += 1
        return
    elif max(map(max, paper)) == min(map(min, paper)) == 1:
        cnt[2] += 1
        return
    elif max(map(max, paper)) == min(map(min, paper)) == -1:
        cnt[0] += 1
        return

    p = N // 3
    sameNumber(p, [row[:p] for row in paper[:p]], cnt)
    sameNumber(p, [row[p:2*p] for row in paper[:p]], cnt)
    sameNumber(p, [row[2*p:] for row in paper[:p]], cnt)

    sameNumber(p, [row[:p] for row in paper[p:2*p]], cnt)
    sameNumber(p, [row[p:2*p] for row in paper[p:2*p]], cnt)
    sameNumber(p, [row[2*p:] for row in paper[p:2*p]], cnt)

    sameNumber(p, [row[:p] for row in paper[2*p:]], cnt)
    sameNumber(p, [row[p:2*p] for row in paper[2*p:]], cnt)
    sameNumber(p, [row[2*p:] for row in paper[2*p:]], cnt)


N = int(sys.stdin.readline().strip())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 0: -, 1: 0, 2: +
cnt = [0] * 3

sameNumber(N, paper, cnt)

print(cnt[0])
print(cnt[1])
print(cnt[2])
