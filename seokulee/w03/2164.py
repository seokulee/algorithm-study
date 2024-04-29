import sys
from collections import deque

N = int(sys.stdin.readline())

d = deque([i for i in range(1, N+1)])

while len(d) > 1:
    d.popleft()
    d.append(d.popleft())

print(d.pop())

