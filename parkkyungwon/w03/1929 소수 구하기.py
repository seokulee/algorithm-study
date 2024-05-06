m, n = map(int, input().split())

SOE = [True for _ in range(n+1)]
SOE[1] = False
for i in range(2, n+1):
    if SOE[i]:
        for j in range(i*2, n+1, i):
            SOE[j] = False

for i in range(m, n+1):
    if SOE[i]:
        print(i)
