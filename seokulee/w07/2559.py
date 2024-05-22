import sys
from itertools import accumulate


def solution():
    N, K = map(int, sys.stdin.readline().split())
    accum = [0, *accumulate(map(int, sys.stdin.readline().split()))]

    section_sum = list()
    for i in range(N - K + 1):
        section_sum.append(accum[i+K] - accum[i])

    return max(section_sum)


if __name__ == '__main__':
    print(solution())
