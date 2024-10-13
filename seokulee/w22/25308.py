import sys
import math
from itertools import permutations


class Point:
    def __init__(self, score=None, order=None, x=None, y=None):
        if x is not None and y is not None:
            self.x = x
            self.y = y
        elif score is not None and order is not None:
            angle = math.pi * (order * 45) / 180
            self.x = score * math.cos(angle)
            self.y = score * math.sin(angle)
        else:
            raise ValueError()

    def __sub__(self, other):
        return Point(x=self.x - other.x, y=self.y - other.y)

    def __str__(self):
        return f'({self.x}, {self.y})'


def crossProduct(A: Point, B: Point):
    return (A.x * B.y) - (B.x * A.y)


# def isNoPostive(points):
#     for i in range(8):
#         p1 = points[i]
#         p2 = points[(i + 1) % 8]
#         p3 = points[(i + 2) % 8]

#         p12 = p2 - p1
#         p23 = p3 - p2

#         if crossProduct(p12, p23) >= 0:
#             return False

#     return True

def isConvex(points):
    num_points = len(points)
    prev_cross = 0
    for i in range(num_points):
        p1 = points[i]
        p2 = points[(i + 1) % num_points]
        p3 = points[(i + 2) % num_points]

        p12 = p2 - p1
        p23 = p3 - p2

        cross = crossProduct(p12, p23)

        if cross != 0:
            if prev_cross != 0 and cross * prev_cross < 0:
                return False
            prev_cross = cross
    return True

# 능력치 입력받기 (정렬)
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 각 능력치 위치는 능력치 * (cos(45*k), sin(45*k))
# 3 꼭지점씩 봤을 떄 외적이 양수면 안됌!

count = 0
for perm in permutations(arr):
    points = [Point(perm[i], i) for i in range(8)]
    if isConvex(points):
        count += 1

print(count)

# 방사형 그래프에서 좌표 설정은  45도씩 차이남. 수학적으로 계산한 뒤, 불등식을 도출해낼 수 있음.
# 순열의 하나를 고정하면 7! 가지로 감소. 8을 곱하는 방법
