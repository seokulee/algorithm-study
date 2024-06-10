def find(n, k):
    def check(m):
        t = 0
        sq = int(m ** 0.5)

        for i in range(1, sq + 1):
            t += min(m // i, n)*2
        return t - sq ** 2


    s, e = 0, k
    while s < e:
        m = (s + e) // 2
        if check(m) < k: s = m + 1
        else: e = m
    
    return s


N = int(input())
K = int(input())

print(find(N, K))
