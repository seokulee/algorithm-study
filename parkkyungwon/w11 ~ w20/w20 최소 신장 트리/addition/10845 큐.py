import sys


readline = sys.stdin.readline
N = int(readline())
queue = [] 

for _ in range(N):
    command = readline().split()
    match command[0]:
        case 'push':
            queue.append(command[1])
            continue
        case 'pop':
            output = queue.pop(0) if queue else -1
        case 'size':
            output = len(queue)
        case 'empty':
            output = 0 if queue else 1
        case 'front':
            output = queue[0] if queue else -1
        case 'back':
            output = queue[-1] if queue else -1
        
    sys.stdout.write(str(output) + '\n')
