import sys



readline = sys.stdin.readline

N = int(readline().strip())
hist = set()
c = 0

for _ in range(N):
    t = readline().strip()

    if t != "ENTER":
        hist.add(t)
    
    else:
        c += len(hist)
        hist = set()
else:
    c += len(hist)

print(c)
