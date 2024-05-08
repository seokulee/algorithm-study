import sys

def star(N):
    if N == 1:
        return ['*']

    stars = star(int(N // 3))
    arr = list()

    for s in stars:
        arr.append(s * 3)
    for s in stars:
        arr.append(s + ' '*(N//3) + s)
    for s in stars:
        arr.append(s * 3)

    return arr



N = int((sys.stdin.readline()))

print('\n'.join(star(N)))
