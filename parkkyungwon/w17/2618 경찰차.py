import sys
from collections import defaultdict



# 두 사건간의 거리를 저장
def get_diff(arr, i):
    i -= 1
    a = sum(arr[i]) - 2
    return [[a, MAX_INDEX-a-2]] + [abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1]) for j in range(i)]


# 최단경로 역 추적
def backtrack(arr, i, j):
    shor_path = []

    for k in range(L-1, 0, -1):
        if i == k:
            shor_path.append(2)
            i = arr[i][j]
        else:
            shor_path.append(1)
            j = arr[i][j]

    return shor_path[::-1]


def sol(incidents):
    dp = {(0, 0): 0}
    hist = [[0] * L for _ in range(L)]
    maxi = float('inf')

    for i in range(1, L):
        dp2 = defaultdict(lambda: float('inf'))
        diff = get_diff(incidents, i)
        maxi2 = maxi + MAX_INDEX - 2
        maxi = float('inf')

        for k, v in dp.items():
            car2, car1 = k
            d1 = (diff[0][0] if car1 == 0 else diff[car1]) + v
            d2 = (diff[0][1] if car2 == 0 else diff[car2]) + v

            if d1 < maxi2 and d1 < dp2[(car2, i)]:
                dp2[(car2, i)] = d1
                hist[car2][i] = car1

            if d2 < maxi2 and d2 < dp2[(i, car1)]:
                dp2[(i, car1)] = d2
                hist[i][car1] = car2
            
            maxi = min(maxi, d1, d2)

        dp = dp2
    
    k, v = sorted(dp.items(), key=lambda x: x[1])[0]
    y, x = k
    
    return [v] + backtrack(hist, y, x)
    
    

readline = sys.stdin.readline
N = int(readline())
W = int(readline())
incidents = [tuple(map(int, readline().split())) for _ in range(W)]

L = W + 1
MAX_INDEX = 2 * N

print(*sol(incidents), sep='\n')
