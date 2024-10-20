import math

# cos a
# (dist - r1*cos(a))**2 + (r1*sin(a))**2 = r2**2
# dist**2 - 2*dist*r1*cos(a) + r1**2*cos**2(a) + r1**2*sin**2(a) = r2**2
# dist**2 - 2*dist*r1*cos(a) + r1**2 = r2**2
# cos(a) = - (r2**2 - r1**2 - dist**2) / (2*dist*r1)

# sin a
# sin(a) = (1 - cos_a**2)**(0.5)

# 부채꼴의 넓이에 활꼴을 뺀 넓이
# 2 * 1/2 * r1*cos(a) * r1*sin(a)
# = r1**2*cos(a)*sin(a)

# 부채꼴 넓이 
# 2 * pi * r1**2 * a / (2pi)
# r1**2 * a 

def arc(r1, r2, dist):
    cos_a = - (r2**2 - r1**2 - dist**2) / (2*dist*r1)
    sin_a = (1 - cos_a**2)**(0.5)

    return r1**2 * (math.acos(cos_a) - cos_a * sin_a)


def sol(data):
    x1, y1, r1, x2, y2, r2 = data

    dist = ((x1-x2)**2 + (y1-y2)**2)**(0.5)

    # 겹치지 않거나, 
    # 두 반지름 중 하나라도 0,
    if dist > r1 + r2 or not all((r1, r2)): return 0
    # 한 원이 다른 원 안에 있을 때
    if max(r1, r2) >= min(r1, r2) + dist: return min(r1, r2)**2 * math.pi

    return arc(r1, r2, dist) + arc(r2, r1, dist)


data = tuple(map(float, input().split()))

print(f'{sol(data):.3f}')
