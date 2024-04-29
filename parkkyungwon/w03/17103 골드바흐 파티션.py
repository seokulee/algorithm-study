import sys



count = int(sys.stdin.readline())

ns = []
for _ in range(count):
    ns.append(int(sys.stdin.readline()))

n_max = max(ns) + 1
SOE = [True for _ in range(n_max)]
SOE[1] = False
primes = []
for i in range(2, n_max):
    if SOE[i]:
        primes.append(i)
        for j in range(i*2, n_max, i):
            SOE[j] = False

for n in ns:
    c = 0
    max_search = n//2
    for prime in primes:
        if prime > max_search:
            break

        if SOE[n-prime] == True:
            c += 1
    
    print(c)
