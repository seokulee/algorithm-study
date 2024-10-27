import sys



def sol(data):
    cumsum = 0

    for n, s in data:
        cumsum += s * pow(n, -1, MOD) % MOD
        cumsum %= MOD
    
    return cumsum


readline = sys.stdin.readline
MOD = int(1e9) + 7

M = int(readline())
data = (map(int, readline().split()) for _ in range(M))

print(sol(data))
