num_l = map(int, input())

num_l = sorted(num_l, reverse=True)
for i in num_l:
    print(i, end='')