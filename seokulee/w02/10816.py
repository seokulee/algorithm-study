import sys

N = int(sys.stdin.readline())
owned = list(map(int, sys.stdin.readline().split()))
owned_dict = dict()

for n in owned:
    if n in owned_dict.keys():
        owned_dict[n] += 1
    else:
        owned_dict[n] = 1

M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

print(' '.join([str(owned_dict[i]) if i in owned_dict.keys() else '0' for i in target]))
