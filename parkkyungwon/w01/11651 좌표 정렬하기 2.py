count = int(input())

coordinates = []
for _ in range(count):
    coordinates.append(tuple(map(int, input().split())))

coordinates.sort(key=lambda x: (x[1], x[0]))

for item in coordinates:
    print(item[0], item[1])
    