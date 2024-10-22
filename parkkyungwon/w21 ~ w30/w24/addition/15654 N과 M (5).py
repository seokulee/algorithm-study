from itertools import permutations as pr
import sys



write = sys.stdout.write
M = int(input().split()[1])
arr = sorted(map(int, input().split()))

for c in pr(arr, M):
    write(' '.join(map(str, c)) + '\n')
