import sys



readline = sys.stdin.readline


c = int(readline())
nums = [int(readline()) for _ in range(c)]
a = [0, 0, 0]
b = [0, 0, 0]

for num in nums:
    a[2] = max(b)
    a[1] = num + b[2]
    a[0] = num + b[1]

    a, b = b, a

sys.stdout.write(str(max(b)) + '\n')









# import sys


# sys.setrecursionlimit(10**6)


# def o_dfs(nums: list):
#     l = len(nums)
#     sums = [[0, 0, 0] for _ in range(l)]

#     def dfs(i, p):
#         if i == 0:
#             if p:
#                 return nums[0]
#             else:
#                 return 0

#         if not sums[i][p]:
#             if p:
#                 sums[i][p] = max(nums[i] + dfs(i-1, p-1), dfs(i-1, 2))
#             else:
#                 sums[i][p] = dfs(i-1, 2)

#         return sums[i][p]
    
#     return dfs(l-1, 2)


# readline = sys.stdin.readline


# c = int(readline())
# nums = [int(readline()) for _ in range(c)]

# sys.stdout.write(str(o_dfs(nums)) + '\n')
