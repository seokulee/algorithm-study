import sys



def sol(distances):
    L = len(distances)

    # k의 위치는 꼭 반복문의 최상위에 있어야함
    for k in range(1, L):
        for i in range(1, L):
            for j in range(1, L):
                w = distances[i][k] + distances[k][j]
                if distances[i][j] > w:
                    distances[i][j] = w


readline = sys.stdin.readline
V = int(readline())
E = int(readline())

distances = tuple([float('inf')] * (V+1) for _ in range(V+1))
for i in range(V + 1):
    distances[i][i] = 0
for a, b, d in (map(int, readline().split()) for _ in range(E)):
    if d < distances[a][b]:
        distances[a][b] = d

sol(distances)

for d in distances[1:]:
    print(*map(lambda x: 0 if x == float('inf') else x, d[1:]))
    