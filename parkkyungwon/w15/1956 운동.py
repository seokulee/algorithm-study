import sys



def floyd(distances):
    L = len(distances)

    for k in range(1, L):
        for i in range(1, L):
            for j in range(1, L):
                w = distances[i][k] + distances[k][j]
                if distances[i][j] > w:
                    distances[i][j] = w


def search(distances):
    L = len(distances)
    mini = float('inf')

    for i in range(1, L):
        for j in range(i+1, L):
            w = distances[i][j] + distances[j][i]
            if w < mini:
                mini = w
    
    return -1 if mini == float('inf') else mini


readline = sys.stdin.readline
V, E = map(int, readline().split())

distances = tuple([float('inf')] * (V+1) for _ in range(V+1))
for i in range(V + 1):
    distances[i][i] = 0

for a, b, d in (map(int, readline().split()) for _ in range(E)):
    distances[a][b] = d

floyd(distances)

print(search(distances))
