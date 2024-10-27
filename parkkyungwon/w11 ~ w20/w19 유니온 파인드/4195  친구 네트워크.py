import sys



class UnionFind():
    def __init__(self, n):
        self.dp = [-1] * (2*n + 1)

    def find(self, i):
        if self.dp[i] < 0: return i

        self.dp[i] = self.find(self.dp[i])

        return self.dp[i]

    def union(self, a, b):
        if a == b: return

        ra, rb = self.find(a), self.find(b)
        if ra == rb: return
        
        if self.dp[ra] < self.dp[rb]: 
            self.dp[ra] += self.dp[rb]
            self.dp[rb] = ra
        else: 
            self.dp[rb] += self.dp[ra]
            self.dp[ra] = rb
    
    def get_size(self, i):
        return self.dp[self.find(i)]


class Indexing():
    def __init__(self):
        self.dictionary = {}
        self.count = 0
    
    def __getitem__(self, i):
        if i not in self.dictionary: 
            self.count += 1
            self.dictionary[i] = self.count

        return self.dictionary[i]


readline = sys.stdin.readline
write = sys.stdout.write
T = int(readline())

for _ in range(T):
    N = int(readline())
    uf = UnionFind(N)
    idxing = Indexing()

    for _ in range(N):
        a, b = readline().split()

        c = idxing[a]
        uf.union(c, idxing[b])

        write(str(-uf.get_size(c)) + '\n')
