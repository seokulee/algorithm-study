import sys


def sameColor(N, paper, result):
    if sum(map(sum, paper)) == 0:
        result.append('0')
        return
    elif sum(map(sum, paper)) == N ** 2:
        result.append('1')
        return

    half = N // 2
    result.append('(')
    sameColor(half, [row[:half] for row in paper[:half]], result)
    sameColor(half, [row[half:] for row in paper[:half]], result)
    sameColor(half, [row[:half] for row in paper[half:]], result)
    sameColor(half, [row[half:] for row in paper[half:]], result)
    result.append(')')


N = int(sys.stdin.readline().strip())
paper = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
result = list()

sameColor(N, paper, result)
print(*result, sep='')
