def sol(arr):
    arr2 = sorted(arr)
    count_dp = {a: 0 for a in arr}
    end = arr2[-1] + 1

    for a in arr2:
        for i in range(a+a, end, a):
            if i in count_dp:
                count_dp[i] -= 1
                count_dp[a] += 1
    
    return [count_dp[a] for a in arr]


N = int(input())
arr = tuple(map(int, input().split()))

print(*sol(arr))
