import sys

N = int(sys.stdin.readline())
s = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

for i in l:
    if i in s:
        print(1)
    else:
        print(0)
