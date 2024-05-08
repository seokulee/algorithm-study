import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

for i in combinations(range(1,N+1), M):
    print(*i)
