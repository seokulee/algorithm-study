import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
d = deque(i for i in range(1, N+1))
result = list()

while(d):
    for _ in range(K-1):
        d.append(d.popleft())
    result.append(d.popleft())

print('<' + ', '.join(map(str, result)) + '>')
