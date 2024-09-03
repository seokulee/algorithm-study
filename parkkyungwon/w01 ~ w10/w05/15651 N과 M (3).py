import sys
import itertools



N, M = map(int, input().split())

for i in itertools.product(range(1, N+1), repeat=M):
    sys.stdout.write(' '.join(map(str, i)) + '\n')
