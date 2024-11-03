import bisect



class Check:
    def __init__(self, n, k):
        self.n, self.k = n, k

    def __getitem__(self, m):
        total = 0
        sq = int(m ** 0.5)

        for i in range(1, sq + 1):
            a = m // i
            total += a if a < self.n else self.n

        return 2*total - sq**2

    def __len__(self):
        return self.k
        

N, K = int(input()), int(input())

print(bisect.bisect_left(Check(N, K), K))
