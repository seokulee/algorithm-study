import sys



readline = sys.stdin.readline
write = sys.stdout.write

readline()
cards = {} 
for v in readline().split():
    cards[v] = cards.get(v, 0) + 1

readline()

for v in readline().split():
    write(str(cards.get(v, 0)) + ' ')
