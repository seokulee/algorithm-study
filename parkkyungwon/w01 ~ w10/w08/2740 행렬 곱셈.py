import sys



readline = sys.stdin.readline
arr = []
for _ in range(2):
    a = int(readline().split()[0])
    arr.append(tuple(tuple(map(int, readline().split())) for _ in range(a)))
arr[1] = tuple(v for v in zip(*arr[1]))

arr2 = tuple(tuple(sum(a*b for a, b in zip(A, B)) for B in arr[1]) for A in arr[0])

for ar in arr2:
    for a in ar:
        sys.stdout.write(str(a) + ' ')
    sys.stdout.write('\n')
