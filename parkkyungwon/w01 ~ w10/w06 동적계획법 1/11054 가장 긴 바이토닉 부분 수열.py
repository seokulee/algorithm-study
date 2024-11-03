import sys



def get_sums(l):
    global nums
    sums = [0 for _ in range(l)]

    def lis(s, e, d=1):
        arr = [0]
        for i in range(s, e, d):
            if arr[-1] < nums[i]:
                arr.append(nums[i])
                
            else:
                s, e = 0, len(arr)
                while s < e:
                    m = (s + e) // 2
                    if arr[m] < nums[i]:
                        s = m + 1
                    else:
                        e = m
                
                arr[s] = nums[i]
            
            sums[i] += len(arr) - 1

    lis(0, l)
    lis(l-1, -1, -1)

    return sums


readline = sys.stdin.readline
l = int(readline())
nums = tuple(map(int, readline().split()))

sums = get_sums(l)

sys.stdout.write(str(max(sums) - 1) + '\n')
