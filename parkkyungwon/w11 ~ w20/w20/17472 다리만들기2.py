import sys
import itertools



class UnionFind():
    def __init__(self, n):
        self.dp = [-1] * n

    def find(self, i):
        if self.dp[i] < 0: return i

        self.dp[i] = self.find(self.dp[i])

        return self.dp[i]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)

        if ra == rb: return False
        
        if self.dp[ra] < self.dp[rb]: 
            self.dp[ra] += self.dp[rb]
            self.dp[rb] = ra
        else: 
            self.dp[rb] += self.dp[ra]
            self.dp[ra] = rb
        
        return True


def numbering_island():
    direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
    island_num = 2 # 섬 번호는 2부터 할당한다

    def dfs(i, j):
        maps[i][j] = island_num

        for di, dj in direction:
            di += i
            dj += j

            if maps[di][dj] == 1:
                dfs(di, dj)

    for i in range(1, YL-1):
        for j in range(1, XL-1):
            if maps[i][j] != 1: continue

            dfs(i, j)

            island_num += 1

    return island_num - 2


def get_edge():
    edges = set()

    for arr in itertools.chain(maps, (v for v in zip(*maps))): # 맵의 가로, 세로 배열
        distance = 0
        prev1, prev2 = 0, 0

        for a in arr:
            if a != prev1: # 배열의 값이 연속되지 않을 때
                if prev2: # 두 섬 사이에 도달하면
                    if distance > 1: edges.add((distance, a, prev2)) 

                else: distance = 0 # 두 섬 사이 거리 계산이 끝나고 초기화

                prev1, prev2 = a, prev1 # a, prev1, prev2 값을 한칸씩 밀어냄
            
            if not a: distance += 1 # 값이 0이면 거리를 1씩 증가
    
    return sorted(edges)


def sol():
    uf = UnionFind(8)
    count = numbering_island() - 1
    cost = 0

    for d, i, j in get_edge(): 
        if uf.union(i, j): 
            cost += d
            count -= 1

            if not count: break
    
    else: return -1

    return cost


readline = sys.stdin.readline
N, M = map(int, readline().split())

YL = N + 2
XL = M + 2

# 맵 태두리를 0으로 채움
maps = [[0] * XL]
maps += [[0] + list(map(int, readline().split())) + [0] for _ in range(N)]
maps += [[0] * XL]

print(sol())
