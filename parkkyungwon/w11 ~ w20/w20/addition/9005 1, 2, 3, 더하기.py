import itertools



def sol(n):
    dp = [1, 2, 4]

    if n < 4: return dp[n-1]

    for _, i in zip(range(n-3), itertools.cycle(range(3))): 
        dp[i] = sum(dp)
    
    return dp[i]


ss = open(0).read().splitlines()

print(*(sol(int(s)) for s in ss[1:]), sep='\n')
