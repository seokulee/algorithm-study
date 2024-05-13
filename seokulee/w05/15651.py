import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())

for i in product(range(1,N+1), repeat=M):
    print(*i)
