import sys



def search(n, arr):
    def check(l):
        t = n
        for i in range(len(arr)):
            share = arr[i] // l
            t -= share

            if not share and t > 0:
                return False

            if t < 1:
                return True
        
        return False


    arr = sorted(arr, reverse=True)
    s, e = 0, arr[0]
    while e - s != 1:
        m = (s + e) // 2

        if check(m):
            s = m
        else:
            e = m

    return e if check(e) else s


readline = sys.stdin.readline
K, N = map(int, readline().split())

arr = tuple(int(readline()) for _ in range(K))

sys.stdout.write(str(search(N, arr)) + '\n')
