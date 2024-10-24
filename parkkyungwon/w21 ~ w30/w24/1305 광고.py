def sol(p):
    p_leng = len(p)
    # dp를 저장하는 기준은 직전까지 맞는 접두사 개수를 저장. 
    # i번째 dp는 i-1까지 맞는 접두사 개수를 저장
    dp = [0] * (p_leng+1)
    i, j = 1, 0

    while i < p_leng:
        if p[i] == p[j]: 
            i += 1
            j += 1
            dp[i] = j
        
        elif not j:
            i += 1

        else:
            j = dp[j]

    return p_leng - dp[-1]


input()
s = input()

print(sol(s))
