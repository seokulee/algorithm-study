import sys

result = 0

N, M = map(int, sys.stdin.readline().split())

S = set()
for _ in range(N):
    S.add(sys.stdin.readline().rstrip())

for _ in range(M):
    input = sys.stdin.readline().rstrip()
    if input in S:
        result += 1

print(result)
## for 2번, set 사용해서 지난 번 제출보다 30배 빠르게 구현..
