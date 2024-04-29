import sys



n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    com = tuple(map(int, sys.stdin.readline().split()))
    if len(com) == 2:
        if com[0] == 1:
            stack.append(com[1])
            
    elif com[0] == 2:
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
            
    elif com[0] == 3:
        print(len(stack))
        
    elif com[0] == 4:
        if len(stack):
            print(0)
        else:
            print(1)
    
    elif com[0] == 5:
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
            