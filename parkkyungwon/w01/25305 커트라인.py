N, k = map(int, input().split())

num_l = map(int, input().split())
num_l = sorted(num_l)

print(num_l[-k])
