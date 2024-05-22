import sys
from itertools import accumulate
from math import comb


def solution():
    N, M = map(int, sys.stdin.readline().split())
    x = list(map(int, sys.stdin.readline().split()))

    # Compute prefix sums
    accum = list(accumulate(x))

    mod = {0: 1}

    for num in accum:
        remainder = num % M
        if remainder in mod:
            mod[remainder] += 1
        else:
            mod[remainder] = 1

    count = 0
    for v in mod.values():
        count += comb(v, 2)

    print(count)


if __name__ == '__main__':
    solution()
