from math import gcd, factorial

def solve():
    N = int(input())
    numbers = [input().strip() for _ in range(N)]
    K = int(input())

    mods = [int(num) % K for num in numbers]
    lengths = [len(num) for num in numbers]
    powers_of_10 = [pow(10, lengths[i], K) for i in range(N)]

    dp = [[0] * K for _ in range(1 << N)]
    dp[0][0] = 1

    for mask in range(1 << N):
        for remainder in range(K):
            if dp[mask][remainder] == 0:
                continue
            for i in range(N):
                if mask & (1 << i) == 0:
                    new_mask = mask | (1 << i)
                    new_remainder = (remainder * powers_of_10[i] + mods[i]) % K
                    dp[new_mask][new_remainder] += dp[mask][remainder]

    total_permutations = dp[(1 << N) - 1][0]
    total_cases = factorial(N)

    if total_permutations == 0:
        print("0/1")
    else:
        divisor = gcd(total_permutations, total_cases)
        print(f"{total_permutations // divisor}/{total_cases // divisor}")


solve()
