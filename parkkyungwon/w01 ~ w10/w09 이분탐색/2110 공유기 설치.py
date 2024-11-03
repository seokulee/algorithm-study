import sys



def find(arr, c):
    def check(n):
        left, total = arr[0], 1

        for v in arr[1:]:
            if v - left < n: continue
            total += 1
            left = v

        return total >= c

    
    arr.sort()

    s, e = 0, (arr[-1] - arr[0]) // (c - 1) + 1
    while s < e:
        m = (s + e) // 2
        if check(m): s = m + 1
        else: e = m
    
    return s-1


readline = sys.stdin.readline

N, C = map(int, readline().split())
arr = [int(readline()) for _ in range(N)]

sys.stdout.write(str(find(arr, C)) + '\n')
