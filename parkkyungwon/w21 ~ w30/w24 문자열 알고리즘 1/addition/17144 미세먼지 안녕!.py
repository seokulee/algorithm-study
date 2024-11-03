import sys
from itertools import chain, cycle
import copy



def sol(arr):
    for i in range(3, R2-3):
        if arr[i][1] == -1: break
    machine_i = i

    dp_tmp = [[0] * C2 for _ in range(R2)]
    for i in range(R2):
        dp_tmp[i][0], dp_tmp[i][-1] = -1, -1
    
    for i in range(C2):
        dp_tmp[0][i], dp_tmp[-1][i] = -1, -1

    for _ in range(T):
        arr2 = copy.deepcopy(dp_tmp)

        # 확산
        for i in range(1, R2-1):
            for j in range(1, C2-1):
                arr2[i][j] += arr[i][j]
                if arr[i][j] < 5: continue
                share = arr[i][j] // 5

                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    di += i
                    dj += j

                    if arr[di][dj] < 0: continue

                    arr2[i][j] -= share
                    arr2[di][dj] += share
        
        # 회전
        first, last = cycle([1]), cycle([-2])
        mc, mc1 = cycle([machine_i]), cycle([machine_i + 1])
        previ, prevj = 0, 0

        for i, j in chain(zip(range(machine_i-1, 0, -1), first),
                          zip(first, range(2, C2-1)),
                          zip(range(2, machine_i+1), last),
                          zip(mc, range(C2-3, 1, -1))):
            arr2[previ][prevj] = arr2[i][j]
            previ, prevj = i, j

        arr2[previ][prevj] = 0
        previ, prevj = 0, 0

        for i, j in chain(zip(range(machine_i+2, R2-1), first),
                          zip(last, range(2, C2-1)),
                          zip(range(R2-3, machine_i, -1), last),
                          zip(mc1, range(C2-3, 1, -1))):
            arr2[previ][prevj] = arr2[i][j]
            previ, prevj = i, j

        arr2[previ][prevj] = 0
        arr2[0][0] = -1
        arr = arr2
    
    return sum(sum(a[1:-1]) for a in arr[1:-1]) + 2


readline = sys.stdin.readline
R, C, T = map(int, readline().split())
R2, C2 = R + 2, C + 2

arr = [[-1] * C2]
for _ in range(R):
    arr += [[-1] + list(map(int, readline().split())) + [-1]]
arr += [[-1] * C2]

print(sol(arr))
