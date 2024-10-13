import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# def getPointDistance(A: Point, B: Point) -> float:
#     return ((A.x - B.x) ** 2 + (A.y - B.y) ** 2) ** 0.5


def crossProduct(A: Point, B: Point):
    return (A.x * B.y) - (B.x * A.y)


N = int(sys.stdin.readline())
points = []

for _ in range(N):
    points.append(Point(*map(int, sys.stdin.readline().split())))

# # 헤론의 공식
# 한계점 : 삼각형을 정확히 나눌 수 있는가? 겹치는 부분이 생길 수 있음
# area = 0
# for i in range(N - 2):
#     l1 = getPointDistance(points[i], points[i + 1])
#     l2 = getPointDistance(points[i + 1], points[i + 2])
#     l3 = getPointDistance(points[i], points[i + 2])

#     s = (l1 + l2 + l3) / 2
#     area += (s * (s - l1) * (s - l2) * (s - l3)) ** 0.5

# print(area)

# 가우스의 면적 공식
points.append(points[0])

# s = 0
# for i in range(N):
#     s += crossProduct(points[i], points[i + 1])

# print(abs(s) / 2)

print(abs(sum(crossProduct(points[i], points[(i + 1) % N]) for i in range(N))) / 2)
