import sys

N = int(sys.stdin.readline())
working = set()

for _ in range(N):
    name, status = sys.stdin.readline().split()
    if status == 'enter':
        working.add(name)
    else:
        working.remove(name)

sorted_arr = sorted(working, reverse=True)

print('\n'.join(sorted_arr))
