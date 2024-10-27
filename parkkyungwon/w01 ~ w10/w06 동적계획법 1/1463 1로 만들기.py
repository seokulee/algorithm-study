import sys



n = int(sys.stdin.readline())
nums = [1000000 for _ in range(n+1)]
nums[n] = 0

for i in range(n, 1, -1):
    next = nums[i] + 1
        
    if i % 3 == 0:
        j = i // 3
        nums[j] = min(nums[j], next)

    if i % 2 == 0:
        j = i // 2
        nums[j] = min(nums[j], next)
    
    nums[i-1] = min(nums[i-1], next)

sys.stdout.write(str(nums[1]) + '\n')





# import sys
# from collections import defaultdict



# n = int(sys.stdin.readline())
# nums = defaultdict(lambda: 1000000)

# prev = 0
# for i in range(n, 1, -1):
#     next = min(nums.get(i, 1000000), prev) + 1
        
#     if i % 3 == 0:
#         j = i // 3
#         nums[j] = min(nums[j], next)

#     if i % 2 == 0:
#         j = i // 2
#         nums[j] = min(nums[j], next)
    
#     prev = next

# sys.stdout.write(str(nums.get(1, 0)) + '\n')
