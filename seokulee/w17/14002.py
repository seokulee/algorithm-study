import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1] * N
path = [[] for _ in range(N)]
for i in range(N):
    path[i] = [arr[i]]

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < (dp[j] + 1):
            dp[i] = dp[j] + 1
            path[i] = path[j] + [arr[i]]

max_length = max(dp)
max_index = dp.index(max_length)

print(max_length)
print(*path[max_index])

# N = int(sys.stdin.readline())
# num = list(map(int, sys.stdin.readline().split()))

# dp = [1]*N

# for i in range(1, N):
#     for j in range(i):
#         if num[i]>num[j]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(max(dp))
# order = max(dp)
# arr = []
# for i in range(N-1, -1, -1):
#     if dp[i]==order:
#         arr.append(num[i])
#         order-=1

# arr.reverse()
# for i in arr:
#     print(i, end=' ')
