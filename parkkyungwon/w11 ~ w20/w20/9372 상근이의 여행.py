import sys


readline = sys.stdin.readline
T = int(readline())

for _ in range(T):
    N, M = map(int, readline().split())

    for _ in range(M): readline()

    sys.stdout.write(str(N-1) + '\n')
