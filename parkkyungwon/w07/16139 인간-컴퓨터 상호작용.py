import sys



readline = sys.stdin.readline
write = sys.stdout.write

arr = readline().strip()
q = int(readline())
n = len(arr)

prefix_sums = {chr(i): [0] * (n + 1) for i in range(97, 123)}

for i in range(n):
    char = arr[i]
    for key in prefix_sums:
        prefix_sums[key][i + 1] = prefix_sums[key][i] + (1 if char == key else 0)

for _ in range(q):
    c, start, end = readline().strip().split()
    start, end = int(start), int(end)
    write(str(prefix_sums[c][end + 1] - prefix_sums[c][start]) + '\n')
