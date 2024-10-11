import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ccw(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    # if val == 0:
    #     return 0  # 일직선상
    if val > 0:
        return 1  # 시계 방향
    else:
        return 2  # 반시계 방향

def on_segment(p, q, r):
    if min(p.x, r.x) <= q.x <= max(p.x, r.x) and \
       min(p.y, r.y) <= q.y <= max(p.y, r.y):
        return True
    return False

def do_intersect(p1, q1, p2, q2):
    # 네 가지 방향성 계산
    o1 = ccw(p1, q1, p2)
    o2 = ccw(p1, q1, q2)
    o3 = ccw(p2, q2, p1)
    o4 = ccw(p2, q2, q1)

    # 일반 케이스
    if o1 != o2 and o3 != o4:
        return True

    # 특수 케이스
    # if o1 == 0 and on_segment(p1, p2, q1):
    #     return True
    # if o2 == 0 and on_segment(p1, q2, q1):
    #     return True
    # if o3 == 0 and on_segment(p2, p1, q2):
    #     return True
    # if o4 == 0 and on_segment(p2, q1, q2):
    #     return True

    return False

# 입력 받기
element1 = list(map(int, sys.stdin.readline().rstrip().split()))
element2 = list(map(int, sys.stdin.readline().rstrip().split()))

# 점 생성
x1, y1, x2, y2 = element1
p1 = Point(x1, y1)
q1 = Point(x2, y2)

x3, y3, x4, y4 = element2
p2 = Point(x3, y3)
q2 = Point(x4, y4)

# 교차 여부 확인 및 출력
if do_intersect(p1, q1, p2, q2):
    print(1)
else:
    print(0)
