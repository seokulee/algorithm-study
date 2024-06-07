import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

P.sort()

result = 0
for i in range(N):
    result += sum(P[:N-i])

print(result)