import sys
from collections import deque

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

C = list(map(int, sys.stdin.readline().split()))

queue = deque()
for i in range(N):
    if not A[i]: # queue 일 떄
        queue.appendleft(B[i])

if queue == []:
    print(*C)
    sys.exit()

for i in range(M):
    queue.append(C[i])
    print(queue.popleft(), end=' ')
