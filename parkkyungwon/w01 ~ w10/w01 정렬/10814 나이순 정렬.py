count = int(input())

coordinates = []
for _ in range(count):
    inputs = input().split()
    coordinates.append((int(inputs[0]), inputs[1]))

coordinates.sort(key=lambda x: x[0])

for item in coordinates:
    print(*item)
    