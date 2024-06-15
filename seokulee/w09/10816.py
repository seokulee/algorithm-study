import sys
from collections import Counter

N = int(sys.stdin.readline())
lst = list(sys.stdin.readline().rstrip().split())
M = int(sys.stdin.readline())
target = list(sys.stdin.readline().rstrip().split())

C = Counter(lst)

result = list()
for t in target:
    result.append(C[t])

print(' '.join(map(str, result)))
