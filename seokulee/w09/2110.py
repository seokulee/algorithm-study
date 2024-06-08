import sys

N, C = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(N)]


def count_c(m):
    c = 1

    cur_house = house[0]
    for i in range(1, N):
        if cur_house + m <= house[i]:
            c += 1
            cur_house = house[i]

    return c


house.sort()
s, e = 0, house[-1] - house[0]

while s <= e:
    m = (s + e) // 2

    if count_c(m) >= C:
        answer = m
        s = m + 1
    else:
        e = m - 1


print(answer)
