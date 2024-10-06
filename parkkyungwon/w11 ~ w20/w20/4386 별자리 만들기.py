import sys
import heapq


class UnionFind():
    def __init__(self, n):
        self.dp = [-1] * n

    def find(self, i):
        if self.dp[i] < 0: return i

        self.dp[i] = self.find(self.dp[i])

        return self.dp[i]

    def union(self, a, b):
        if a == b: return False

        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False
        
        if self.dp[ra] < self.dp[rb]: 
            self.dp[ra] += self.dp[rb]
            self.dp[rb] = ra
        else: 
            self.dp[rb] += self.dp[ra]
            self.dp[ra] = rb
        
        return True

    def get_size(self, i):
        return -self.dp[self.find(i)]


def set_heapq(arr, uf):
    L = len(arr)
    heap = []

    for i in range(1, L-1):
        ay = arr[i][0]
        ax = arr[i][1]
        group = uf.find(i)

        for j in range(i+1, L):
            # 이미 연결되어 있으면 패스
            if uf.find(j) == group: continue

            # 제곱근은 간선을 선택한 뒤 계산
            d = (ay - arr[j][0])**2 + (ax - arr[j][1])**2

            heapq.heappush(heap, (d, i, j))
    
    return heap


def get_mst(heap, uf, count):
    cost = 0.0

    # 간선 가중치 오름차순으로 뽑고, 사이클이 생기지 않는 n-1개를 선택
    while 1:
        d, i, j = heapq.heappop(heap)

        if uf.union(i, j):
            # 제곱근 계산
            cost += d**(0.5)

            if uf.get_size(i) == count: break
    
    return cost


def sol(arr, uf):
    heap = set_heapq(arr, uf)
    
    return get_mst(heap, uf, len(arr) - 1)


readline = sys.stdin.readline
N, M = map(int, readline().split())

# 인덱스 계산하기 쉽게 0 인덱스에 더미 추가
coor = [0] + [tuple(map(int, readline().split())) for _ in range(N)]
uf = UnionFind(N+1)

for _ in range(M):
    uf.union(*map(int, readline().split()))

print(f'{sol(coor, uf):.2f}')