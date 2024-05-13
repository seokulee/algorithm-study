import sys
from itertools import combinations

N = int(sys.stdin.readline())
synerge = list()
score_gap = list()

for _ in range(N):
    synerge.append(list(map(int, sys.stdin.readline().split())))

for t1 in combinations(range(N), N//2):
    t2 = [i for i in range(N) if i not in t1]

    t1_score = 0
    for a, b in combinations(t1, 2):
        t1_score += synerge[a][b]
        t1_score += synerge[b][a]
    t2_score = 0
    for a, b in combinations(t2, 2):
        t2_score += synerge[a][b]
        t2_score += synerge[b][a]

    score_gap.append(abs(t2_score - t1_score))

print(min(score_gap))
