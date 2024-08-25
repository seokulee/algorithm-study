import sys
import bisect
from itertools import combinations

N, C = map(int, (sys.stdin.readline().split()))
W = list(map(int, (sys.stdin.readline().split())))

def mitm(N, C, W):
    if N == 1 and W[0] <= C:
        return 2
    if N == 1 and W[0] > 0:
        return 1

    left, right = W[:N//2], W[N//2:]
    sub_a, sub_b = [0],[0]

    for i in range(1,len(left)+1):
        for sub in combinations(left,i):
            sub_a.append(sum(sub))
    sub_a = sorted(sub_a)

    for i in range(1,len(right)+1):
        for sub in combinations(right,i):
            sub_b.append(sum(sub))
    sub_b = sorted(sub_b)

    answer = 0

    for i in sub_a:
        if C - i < 0:
            continue

        idx = bisect.bisect_right(sub_b, C - i)
        answer += idx

    return answer

print(mitm(N, C, W))
