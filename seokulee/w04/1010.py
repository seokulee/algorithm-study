import sys
import math

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(math.comb(M, N))
