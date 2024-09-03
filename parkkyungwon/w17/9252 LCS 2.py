def sol(a, b):
    a = ' ' + a
    b = ' ' + b
    dp = tuple([0] * len(a) for _ in range(len(b)))

    for i in range(1, len(b)):
        for j in range(1, len(a)):
            if b[i] == a[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            
            elif dp[i][j-1] < dp[i-1][j]:
                dp[i][j] = dp[i-1][j]

            else:
                dp[i][j] = dp[i][j-1]

    answer = []

    while i != 0 and j != 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        
        elif dp[i][j] == dp[i][j-1]:
            j -= 1

        else:
            answer.append(a[j])
            i -= 1
            j -= 1

    return len(answer), answer[::-1]


A = input()
B = input()

leng, answer = sol(A, B)
print(leng)
print(*answer, sep=' ')
