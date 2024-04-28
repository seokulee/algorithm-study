num_list = []
for _ in range(5):
    num_list.append(int(input()))

print(sum(num_list) // 5)
print(sorted(num_list)[2])