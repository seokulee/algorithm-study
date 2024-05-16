import sys

N = int(sys.stdin.readline())
wires = list()

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    wires.append((a, b))

wires.sort()

connection = [1 for _ in wires]

for i in range(1, N):
    for j in range(i):
        if wires[j][1] < wires[i][1]:
            connection[i] = max(connection[i], connection[j] + 1)

print(N - max(connection))
