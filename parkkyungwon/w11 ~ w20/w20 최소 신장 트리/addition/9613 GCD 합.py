import itertools
import sys


dp = {}
def gcd(a, b):
    key = (a, b)

    if key in dp: 
        pass

    elif not b:
        dp[key] = a
    
    else:
        dp[key] = gcd(b, a % b)

    return dp[key]

for s in open(0).read().splitlines()[1:]:
    sys.stdout.write(str(sum(gcd(*v) for v in itertools.combinations(map(int, s.split()[1:]), 2))) + '\n')
