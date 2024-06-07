import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))


s, e = 0, max(trees)

while s <= e:
    m = (s + e) // 2

    t = 0
    for tree in trees:
        if tree > m:
            t += tree - m
        # 밑의 방법으로 쓰면 오버헤드가 심한지 시간 초과가 뜬다.
        # t += max(0, tree - m)

    if t >= M:
        s = m + 1
    else:
        e = m - 1

print(e)