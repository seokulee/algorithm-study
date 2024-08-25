def sol(n):
    dp = [float('inf')] * (n+1)
    dp[1] = 0

    for i in range(1, n):
        v = dp[i] + 1
        for j in i*3, i*2, i+1:
            if j <= n and v < dp[j]:
                dp[j] = v
    
    # 도착지에서 출발지로 역순으로 경로를 찾는다
    count = dp[n] - 1
    answer = [n]
    i = n

    for _ in range(dp[n]):
        for a, b in zip((i % 3 == 0, i % 2 == 0, True), (i // 3, i // 2, i - 1)):
            if a and dp[b] == count:
                answer.append(b)
                count -= 1
                i = b
                break
    
    return dp[n], answer
        

N = int(input())

leng, path = sol(N)

print(leng)
print(*path)
