import sys
import itertools



def get_count(arr, t_i):
    t_v = arr[t_i]
    count = sum(map(lambda x: t_v < x, arr))

    # 10을 추가는 중요도가 1개만 존재하면 next(vs)에 오류 발생
    arr += [10]
    L = len(arr)
    vs = iter(sorted(set(arr), reverse=True))
    v = next(vs)

    for i in itertools.cycle(range(L-1, -1, -1)):
        if arr[i] == v:
            v = next(vs) # 10을 추가하지 않았다면 오류가 발생
            if v == t_v: break
    
    for j in itertools.chain(range(i, L), range(0, i)):
        if arr[j] == t_v: count += 1
        if j == t_i: break
    
    return count


readline = sys.stdin.readline
T = int(readline())

for _ in range(T):
    N, target = map(int, readline().split())
    arr = list(map(int, readline().split()))
    
    print(get_count(arr, target))
