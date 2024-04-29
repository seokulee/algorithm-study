import sys
from collections import deque



n = int(sys.stdin.readline())

stack = deque()
for _ in range(n):
    com = tuple(map(int, sys.stdin.readline().split()))
    if len(com) == 2:
        if com[0] == 1:
            stack.appendleft(com[1])
        
        elif com[0] == 2:
            stack.append(com[1])
            
    elif com[0] == 3:
        if len(stack):
            print(stack.popleft())
        else:
            print(-1)
    
    elif com[0] == 4:
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
            
    elif com[0] == 5:
        print(len(stack))
        
    elif com[0] == 6:
        if len(stack):
            print(0)
        else:
            print(1)
    
    elif com[0] == 7:
        if len(stack):
            print(stack[0])
        else:
            print(-1)
    
    elif com[0] == 8:
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
            