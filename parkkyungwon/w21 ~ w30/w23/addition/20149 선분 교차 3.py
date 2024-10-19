def find_point(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    a1, b1 = y2 - y1, x1 - x2
    a2, b2 = y4 - y3, x3 - x4

    c1 = x1*a1 + y1*b1
    c2 = x3*a2 + y3*b2

    denom = a1*b2 - a2*b1

    x = (c1*b2 - c2*b1) / denom
    y = (c2*a1 - c1*a2) / denom

    return x, y


# 1차원 선 위에 a-b 범위에 c가 어디 있는지 출력
# 범위 안이면 양수
# 범위 밖이면 음수
# 범위 끝에 걸쳐있으면 0
def pir(a, b ,c):
    return (c - a) * (b - c)


def ccw(x1, y1, x2, y2, x3, y3):
    vx1, vy1 = x2 - x1, y2 - y1
    vx2, vy2 = x3 - x2, y3 - y2

    return vx1*vy2 - vy1*vx2


def sol(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    a, b = ccw(x1, y1, x2, y2, x3, y3), ccw(x1, y1, x2, y2, x4, y4)
    c, d = ccw(x3, y3, x4, y4, x1, y1), ccw(x3, y3, x4, y4, x2, y2)

    det1, det2 = a*b, c*d

    # 교차하지 않을 때
    if det1 > 0 or det2 > 0: return [0]

    # 한 점만 다른 선분 위에 있을 경우
    if not a and b: return 1, x3, y3
    if a and not b: return 1, x4, y4
    if not c and d: return 1, x1, y1
    if c and not d: return 1, x2, y2

    # 두 선분이 직선 위에 있는 경우
    if not any((a, b, c, d)): 
        # 기울기가 존재하면 x를 사용하고 없으면 y를 사용
        if x1 != x2:
            t1, t2, t3, t4 = x1, x2, x3, x4
        else:
            t1, t2, t3, t4 = y1, y2, y3, y4

        a, b = pir(t1, t2, t3), pir(t1, t2, t4)
        c, d = pir(t3, t4, t1), pir(t3, t4, t2)
        
        # 한 점 이상 다른 선분 안에 있거나, 두 선분의 끝 점이 같을 경우
        if (any(map(lambda x: x > 0, (a, b, c, d))) or not any((a, b, c, d))): return [1]

        # 한 점만 다른 선분 끝에 걸쳐있을 경우
        if t1 == t3 or t1 == t4: return 1, x1, y1
        if t2 == t3 or t2 == t4: return 1, x2, y2

        return [0]

    return 1, *find_point(line1, line2)


line1 = tuple(map(int, input().split()))
line2 = tuple(map(int, input().split()))

answer = sol(line1, line2)

if len(answer) == 1:
    print(answer[0])

else:
    print(answer[0])
    print(*answer[1:])
