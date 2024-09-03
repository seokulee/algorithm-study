import sys
import itertools



N, M = map(int, input().split())

for i in itertools.permutations(range(1, N+1), M):
    for j in i:
        sys.stdout.write(str(j) + ' ')
    sys.stdout.write('\n')
