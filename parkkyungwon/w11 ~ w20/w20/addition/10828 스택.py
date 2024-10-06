import sys

readline = sys.stdin.readline
N = int(readline())
stack = []

for _ in range(N):
    command = readline().split()
    match command[0]:
        case 'push':
            stack.append(command[1])
            continue
        case 'pop':
            output = stack.pop() if stack else -1
        case 'size':
            output = len(stack)
        case 'empty':
            output = 0 if stack else 1
        case 'top':
            output = stack[-1] if stack else -1
        
    sys.stdout.write(str(output) + '\n')
