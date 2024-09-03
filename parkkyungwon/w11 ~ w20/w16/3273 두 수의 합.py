def sol(arr, x):
    s = 0
    e = len(arr) - 1
    count = 0

    while s != e:
        a = arr[s] + arr[e]
        if a == x:
            count += 1
            s += 1
        elif a < x:
            s += 1
        else:
            e -= 1

    return count


input()
arr = sorted(map(int, input().split()))
x = int(input())

print(sol(arr, x))
