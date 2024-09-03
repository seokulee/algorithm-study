import bisect



def find(N, M, memories, costs):
    max_cost = sum(costs)

    dp = [0] * (max_cost + 1)
    
    for i in range(N):
        memory = memories[i]
        cost = costs[i]

        for j in range(max_cost, cost - 1, -1):
            v = dp[j - cost] + memory

            if v > dp[j]:
                dp[j] = v
    
    return bisect.bisect_left(dp, M)


N, M = map(int, input().split())
memories = (*map(int, input().split()), )
costs = (*map(int, input().split()), )

print(find(N, M, memories, costs))
