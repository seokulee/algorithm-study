import sys


N, M = map(int, sys.stdin.readline().split())

arr = []

def loop(start):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(start, N+1):
        arr.append(i)
        loop(i)
        arr.pop()

loop(1)
