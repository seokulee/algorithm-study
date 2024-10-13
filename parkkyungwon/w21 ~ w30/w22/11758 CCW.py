ss = open(0).read().splitlines()
ss = [tuple(map(int, s.split())) for s in ss]

vectors = [(ss[i+1][0]-ss[i][0], ss[i+1][1]-ss[i][1]) for i in range(2)]
det = vectors[0][0]*vectors[1][1] - vectors[0][1]*vectors[1][0]

print(-1 if det < 0 else 0 if det == 0 else 1)
