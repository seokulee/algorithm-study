ss = open(0).read().splitlines()
N = int(ss[0])

ss = [tuple(map(int, s.split())) for s in ss[1:]]
total = sum(ss[i-1][0] * ss[i][1] - ss[i][0] * ss[i-1][1] for i in range(N))

print(round(abs(total) / 2 + 0.000000000000001, 1))
