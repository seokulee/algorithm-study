import sys

count = int(sys.stdin.readline().strip())

n_list = []
for _ in range(count):
    n_list.append(int(sys.stdin.readline().strip()))

n_list = sorted(n_list)

for i in n_list:
    print(i)