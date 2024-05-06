import sys
from collections import deque

N = int(sys.stdin.readline())
arr = deque()

for _ in range(N):
    input = sys.stdin.readline().rstrip()
    if ' ' in input:
        input, param = map(int, (input.split()))
    else:
        input = int(input)
    if input == 1:
        arr.appendleft(param)
    elif input == 2:
        arr.append(param)
    elif input == 3:
        print(-1 if len(arr) == 0 else arr.popleft())
    elif input == 4:
        print(-1 if len(arr) == 0 else arr.pop())
    elif input == 5:
        print(len(arr))
    elif input == 6:
        print(1 if len(arr) == 0 else 0)
    elif input == 7:
        print(-1 if len(arr) == 0 else arr[0])
    elif input == 8:
        print(-1 if len(arr) == 0 else arr[-1])
