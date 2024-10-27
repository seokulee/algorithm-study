import sys


readline = sys.stdin.readline
T = int(readline())

for _ in range(T):
    count = {}
    total = 1

    for s in (readline().split()[1] for _ in range(int(readline()))):
        if s in count: count[s] += 1
        else: count[s] = 1

    for v in count.values():
        total *= v + 1    
    total -= 1

    sys.stdout.write(f'{total}\n')
