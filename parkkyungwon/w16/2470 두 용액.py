def sol(arr):
    s = 0
    e = len(arr) - 1
    mini = float('inf')
    nearest = [0] * 2

    while s != e:
        a = arr[s] + arr[e]
        b = -a if a < 0 else a

        if b < mini:
            mini = b
            nearest[0], nearest[1] = s, e
        
        if a < 0:
            s += 1
        else:
            e -= 1

    return arr[nearest[0]], arr[nearest[1]]


input()
arr = sorted(map(int, input().split()))

print(*sol(arr))
