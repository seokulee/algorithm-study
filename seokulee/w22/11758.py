import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)



def crossProduct(A: Point, B: Point):
    return (A.x * B.y) - (B.x * A.y)


points = []
for _ in range(3):
    points.append(Point(*map(int, sys.stdin.readline().split())))


vec = crossProduct(points[1] - points[0], points[2] - points[1])

if vec > 0:
    print(1)
elif vec < 0:
    print(-1)
else:
    print(0)
