import sys



def o_dfs(nums):
    l = len(nums)
    sums = [0 for i in range(l)]
    
    def dfs(i):
        if sums[i]:
            return sums[i]

        for j in range(i+1, l):
            if nums[i] < nums[j]:
                sums[i] = max(sums[i], dfs(j))
        
        sums[i] += 1
        
        return sums[i]

    for i in range(l):
        dfs(i) 

    return max(sums)


readline = sys.stdin.readline


readline()
nums = tuple(map(int, readline().split()))

sys.stdout.write(str(o_dfs(nums)) + '\n')
