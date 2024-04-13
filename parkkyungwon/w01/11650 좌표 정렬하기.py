count = int(input())

coordinates = [tuple(map(int, input().split())) for _ in range(count)]

coordinates.sort()

for item in coordinates:
    print(item[0], item[1])
    