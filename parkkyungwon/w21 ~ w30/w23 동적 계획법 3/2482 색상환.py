def sol(n, k):
    if k == 0: return 1
    # k가 음수거나 (n+1) / 2 보다 크면 0 반환 
    elif k < 0 or ((n + 1) // 2) < k: return 0

    dp = [1] * n

    for _ in range(k-1):
        n -= 2

        for i in range(1, n+1):
            dp[i] = (dp[i] + dp[i-1]) % 1000000003
    
    return sum(dp[:n]) 


N, K = int(input()), int(input())

# 1번 째 상자와 n번 째 상자를 선택한 경우를 계산해 빼준다
a = (sol(N, K) - sol(N-4, K-2)) % 1000000003

print(a)
