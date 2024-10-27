class UnionFind():
    def __init__(self, n):
        self.dp = [-1] * n

    def find(self, i):
        if self.dp[i] < 0: return i

        self.dp[i] = self.find(self.dp[i])

        return self.dp[i]

    def union(self, a, b):
        ar, br = self.find(a), self.find(b)

        if ar == br: return

        if self.dp[ar] > self.dp[br]:
            self.dp[ar] += self.dp[br]
            self.dp[br] = ar
        else:
            self.dp[br] += self.dp[ar]
            self.dp[ar] = br
    
    def size(self, i):
        return -self.dp[i]


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1)*(y3 - y2) - (x3 - x2)*(y2 - y1)


def pir(a, b, c):
    return (a - c) * (c - b)


def sol(arr):
    uf = UnionFind(N)

    for i in range(N):
        x1, y1, x2, y2 = arr[i]
        ir = uf.find(i)

        for j in range(i, N):
            if ir == uf.find(j): continue

            x3, y3, x4, y4 = arr[j]

            c1, c2 = ccw(x1, y1, x2, y2, x3, y3), ccw(x1, y1, x2, y2, x4, y4)
            c3, c4 = ccw(x3, y3, x4, y4, x1, y1), ccw(x3, y3, x4, y4, x2, y2)

            # 모든 점이 일직선 상에 있는 경우
            if not any((c1, c2, c3, c4)):
                # 기울기가 존재하면 x를 사용하고 없으면 y를 사용
                if x1 != x2: t1, t2, t3, t4 = x1, x2, x3, x4
                else: t1, t2, t3, t4 = y1, y2, y3, y4

                p1, p2 = pir(t1, t2, t3), pir(t1, t2, t4)
                p3, p4 = pir(t3, t4, t1), pir(t3, t4, t2)

                if any(map(lambda x: x >= 0, (p1, p2, p3, p4))): uf.union(i, j)

            elif c1 * c2 <= 0 and c3 * c4 <= 0: uf.union(i, j)

    num_group = len(set(uf.find(i) for i in range(N)))
    max_size = max(uf.size(i) for i in range(N))

    return num_group, max_size


readline = open(0).readline
N = int(readline())
arr = [tuple(map(int, readline().split())) for _ in range(N)]

print(*sol(arr), sep='\n')
