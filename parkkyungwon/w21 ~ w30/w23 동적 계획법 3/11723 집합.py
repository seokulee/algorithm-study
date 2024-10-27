import sys


readline = sys.stdin.readline


def sol():
    M = int(readline())
    bitmask = 0

    for _ in range(M):
        op = readline().split()

        if len(op) == 2:
            op[1] = 1 << int(op[1])

        match op[0]:
            case 'add':     bitmask |= op[1]
            case 'remove':  bitmask &= ~op[1]
            case 'check':   sys.stdout.write('1\n' if (bitmask & op[1]) else '0\n')
            case 'toggle':  bitmask ^= op[1]
            case 'all':     bitmask = ~0
            case _:         bitmask = 0

sol()
