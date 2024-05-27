import sys
from itertools import accumulate


def solution():
    N, M = map(int, sys.stdin.readline().split())
    accum = [0]
    accum.extend(list(accumulate(map(int, sys.stdin.readline().split()))))

    for _ in range(M):
        i, j = map(int, sys.stdin.readline().split())
        print(accum[j] - accum[i - 1])


if __name__ == '__main__':
    solution()
