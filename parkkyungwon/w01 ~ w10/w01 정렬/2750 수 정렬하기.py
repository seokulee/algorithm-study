count = int(input())

n_list = []
for _ in range(count):
    n_list.append(int(input()))

n_list = sorted(n_list)

for i in n_list:
    print(i)