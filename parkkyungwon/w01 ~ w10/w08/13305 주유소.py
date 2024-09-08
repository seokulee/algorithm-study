input()
dis = tuple(map(int, input().split()))
cities = tuple(map(int, input().split()))

c = cities[0]
t = 0
for a, b in zip(dis, cities[1:]):
    t += c * a
    if c > b:
        c = b

print(t)
