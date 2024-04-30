import sys
from collections import defaultdict


readline = sys.stdin.readline
writeline = sys.stdout.write

N, M = map(int, readline().strip().split())
word = defaultdict(lambda: 0)

for _ in range(N):
    w = readline().strip()

    if len(w) < M:
        continue

    word[w] += 1

for w in sorted(word.keys(), key=lambda x: (-word[x], -len(x), x)):
    writeline(w + '\n')
