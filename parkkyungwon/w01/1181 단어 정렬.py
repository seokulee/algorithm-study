count = int(input())

coordinates = set()
for _ in range(count):
    coordinates.add(input())

coordinates = list(coordinates)
coordinates.sort(key=lambda x: (len(x), x))

for item in coordinates:
    print(item)
    