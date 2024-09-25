import sys

readline = sys.stdin.readline
N = int(readline())
bitmask = 0

for _ in range(N):
    command = readline().split()
    
    if len(command) == 2: 
        v = 1 << (int(command[1]) - 1)
    
    match command[0]:
        case 'add':
            bitmask |= v
        case 'remove':
            bitmask &= ~v
        case 'check':
            sys.stdout.write('1\n' if v & bitmask else '0\n')
        case 'toggle':
            bitmask ^= v
        case 'all':
            bitmask = -1
        case 'empty':
            bitmask = 0
            