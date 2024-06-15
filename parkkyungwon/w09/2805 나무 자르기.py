import sys



def search(n, arr):
    def check_i(i):
        a = sums[i+1] - (arr[i] * (len(arr) - i - 1))
        
        return a >= n


    def check_v(v):
        t = target_sum - (v * leng)
        
        return t >= n


    arr = sorted(arr)
    sums = arr[:]
    for i in range(len(sums)-2, -1, -1):
        sums[i] += sums[i+1]

    s, e = 0, len(arr) - 1
    while s != e:
        m = (s + e) // 2

        if check_i(m):
            s = m + 1
        else:
            e = m

    leng = len(arr) - s
    target_sum= sums[s]
    s, e = 0, arr[s]
    while s != e:
        m = (s + e) // 2

        if check_v(m):
            s = m + 1
        else:
            e = m

    return s - 1


readline = sys.stdin.readline

_, N = map(int, readline().split())
arr = tuple(map(int, readline().split()))

sys.stdout.write(str(search(N, arr)) + '\n')
