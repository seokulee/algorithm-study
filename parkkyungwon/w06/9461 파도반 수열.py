import sys



def dp():
    arr = [0 for _ in range(101)]
    arr[1] = arr[2] = arr[3] = 1
    arr[4] = arr[5] = 2
    arr[6], arr[7], arr[8] = 3, 4, 5

    def s_dp(n):
        if not arr[n]: arr[n] = s_dp(n-1) + s_dp(n-5)
        return arr[n]
    
    return s_dp


readline = sys.stdin.readline
find = dp()


C = int(readline())

for _ in range(C):
    N = int(readline())

    sys.stdout.write(str(find(N)) + '\n')
