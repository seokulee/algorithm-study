import sys

N = int(sys.stdin.readline())

dance = set()
dance.add('ChongChong')

for _ in range(N):
    A, B = sys.stdin.readline().split()
    if A in dance:
        dance.add(B)
    elif B in dance:
        dance.add(A)

print(len(dance))
