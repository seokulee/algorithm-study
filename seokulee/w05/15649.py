import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

for i in permutations(range(1,N+1), M):
    print(*i)
