import sys

count = int(sys.stdin.readline().strip())

count_list = [0 for _ in range(10001)]
for _ in range(count):
    count_list[int(sys.stdin.readline().strip()) - 1] += 1

for n, count in enumerate(count_list):
    for _ in range(count):
        print(n + 1)