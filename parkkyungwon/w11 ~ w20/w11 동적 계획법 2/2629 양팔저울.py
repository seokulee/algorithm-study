from collections import defaultdict



def dp(weights, balls):
    dup = defaultdict(set)
    L = len(weights)

    def f(i, current):
        if current in dup[i]:
            return

        dup[i].add(current)

        if i == L:
            return

        f(i+1, abs(current - weights[i]))
        f(i+1, current)
        f(i+1, current + weights[i])
    
    f(0, 0)
    dup = set(v for vs in dup.values() for v in vs)

    return ' '.join('Y' if ball in dup else 'N' for ball in balls)


input()
weights = (*map(int, input().split()), )
input()
balls = (*map(int, input().split()), )

print(dp(weights, balls))
