import sys
from collections import deque

N = int(sys.stdin.readline())
arr = deque()

for _ in range(N):
    input = sys.stdin.readline().rstrip()
    if ' ' in input:
        input, param = input.split()
    if input == 'push':
        arr.append(param)
    elif input == 'pop':
        print(-1 if len(arr) == 0 else arr.popleft())
    elif input == 'size':
        print(len(arr))
    elif input == 'empty':
        print(1 if len(arr) == 0 else 0)
    elif input == 'front':
        print(-1 if len(arr) == 0 else arr[0])
    elif input == 'back':
        print(-1 if len(arr) == 0 else arr[-1])
