def sol(arr):
    L = len(arr)
    counts = [0] * L
    edge = [0] * L

    for i in range(1, L):
        for j in range(i):
            if arr[j] >= arr[i]:
                continue

            k = counts[j] + 1
            if k > counts[i]:
                counts[i] = k
                edge[i] = j
            
    count = max(counts)
    for i in range(L-1, 0, -1):
        if counts[i] == count:
            break
    
    answer = (arr[i], ) + tuple(arr[i := edge[i]] for _ in range(count-1))

    return count, answer[::-1]


input()
arr = (0, ) + tuple(map(int, input().split()))

count, answer = sol(arr)

print(count)
print(*answer)
