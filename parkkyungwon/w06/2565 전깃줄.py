import sys



readline = sys.stdin.readline
l = int(readline())

nums = [tuple(map(int, readline().split())) for _ in range(l)]
nums.sort()

arr = [0]
for num in nums:
    if arr[-1] < num[1]:
        arr.append(num[1])
        
    else:
        s, e = 0, len(arr)
        while s < e:
            m = (s + e) // 2
            if arr[m] < num[1]:
                s = m + 1
            else:
                e = m
        
        arr[s] = num[1]

sys.stdout.write(str(l - len(arr) + 1) + '\n')
