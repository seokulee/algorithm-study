ns = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        ns.append(n)

n_max = max(ns)*2 + 1
SOE = [True for _ in range(n_max)]
SOE[1] = False
for i in range(2, n_max):
    if SOE[i]:
        for j in range(i*2, n_max, i):
            SOE[j] = False

for n in ns:
    c = 0
    for i in range(n+1, n*2+1):
        if SOE[i]:
            c += 1
    
    print(c)
