import sys



def floyd(N, edges):
    for k in range(N):
        for i in range(N):
            if not edges[i][k]: continue

            for j in range(N):
                if edges[k][j]:
                    edges[i][j] = 1


arr = sys.stdin.read().splitlines()
N = int(arr[0])
edges = [list(map(int, a.split())) for a in arr[1:]]

floyd(N, edges)

for e in edges:
    sys.stdout.write(' '.join(map(str, e)) + '\n')
