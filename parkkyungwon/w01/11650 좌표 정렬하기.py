count = int(input())

coordinates = []
for _ in range(count):
    coordinates.append(tuple(map(int, input().split())))

coordinates.sort()

for item in coordinates:
    print(item[0], item[1])
    