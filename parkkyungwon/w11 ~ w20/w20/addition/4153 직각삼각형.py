import sys

while 1:
    arr = tuple(map(lambda x: int(x)**2, sys.stdin.readline().split()))

    if not any(arr): break

    sys.stdout.write('right\n' if 2*max(arr) == sum(arr) else 'wrong\n')
