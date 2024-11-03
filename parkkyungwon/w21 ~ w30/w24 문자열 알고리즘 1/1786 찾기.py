def get_dp(p):
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

    return dp


def sol(t, p):
    dp = get_dp(p)
    ti, pi = 0, 0
    t_leng = len(t)
    p_leng = len(p)
    answer = []

    while ti < t_leng:
        if t[ti] == p[pi]:
            ti += 1
            pi += 1

            if pi == p_leng:
                answer.append(ti - p_leng + 1)
                pi = dp[-1]

        elif not pi:
            ti += 1

        else:
            pi = dp[pi]

    return len(answer), answer


T = input()
P = input()

leng, answers = sol(T, P)

print(leng)
if answers: print(*answers)
