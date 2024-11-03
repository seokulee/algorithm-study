def sol(arr):
    s, e = 0, len(arr)-1
    mini = float('inf')

    while s < e:
        v = arr[s] + arr[e]

        if (v2 := abs(v)) < mini: 
            answer = (s, e)
            mini = v2

            if not v2: break

        if v < 0: s += 1
        else: e -= 1

    return arr[answer[0]], arr[answer[1]]


input()
arr = tuple(map(int, input().split()))

print(*sol(arr))
