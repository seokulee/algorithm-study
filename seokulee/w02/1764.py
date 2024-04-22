import sys

N, M = map(int, sys.stdin.readline().split())

x_heard = set()
x_saw = set()

for _ in range(N):
    x_heard.add(sys.stdin.readline().rstrip())

for _ in range(M):
    x_saw.add(sys.stdin.readline().rstrip())

x_heard_saw = sorted(x_heard.intersection(x_saw))

print(len(x_heard_saw))
for name in x_heard_saw:
    print(name)
