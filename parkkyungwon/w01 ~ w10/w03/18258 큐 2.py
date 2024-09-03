import sys
from collections import deque


readline = sys.stdin.readline

n = int(readline())

stack = deque()
for _ in range(n):
    com = readline().split()
    if com[0] == 'push':
        stack.append(int(com[1]))
            
    elif com[0] == 'pop':
        if len(stack):
            print(stack.popleft())
        else:
            print(-1)
            
    elif com[0] == 'size':
        print(len(stack))
        
    elif com[0] == 'empty':
        if not len(stack):
            print(1)
        else:
            print(0)
    
    elif com[0] == 'front':
        if len(stack):
            print(stack[0])
        else:
            print(-1)

    elif com[0] == 'back':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
            