import sys

poket_count, answer_count = map(int, input().split())

n_to_i = {}
i_to_n = {}
for i in range(1, poket_count + 1):
    name = sys.stdin.readline().strip()
    n_to_i[name] = i
    i_to_n[i] = name

for _ in range(answer_count):
    a = sys.stdin.readline().strip()
    if a[0] in "0123456789":
        print(i_to_n[int(a)])
    else:
        print(n_to_i[a])
