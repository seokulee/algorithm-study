def is_overlap(a, b, c, d):
    if a > b: gr, ls = a, b
    else: gr, ls = b, a

    if ls <= c <= gr or ls <= d <= gr or (c > gr and d < ls) or (c < ls and d > gr): return True
    else: return False


def sol(line1, line2):
    for _ in range(2):
        x1, y1, x2, y2 = line1
        x3, y3, x4, y4 = line2
        arr = []

        t1x, t1y = (x1 - x2), (y1 - y2)
        for v1x, v1y in ((t1x, t1y), (-t1x, -t1y)):

            for t2x, t2y in zip((x3, x4), (y3, y4)):
                v2x, v2y = (x2 - t2x), (y2 - t2y)

                det = v1x*v2y - v1y*v2x

                arr.append(1 if det > 0 else 0 if det == 0 else -1)

        # 모든 점이 직선 위에 있을 때
        if not any(arr):
            if is_overlap(x1, x2, x3, x4) and is_overlap(y1, y2, y3, y4): return 1
            else: return 0

        for det in (arr[0] * arr[1]), (arr[2] * arr[3]), (arr[0] * arr[2]):
            if det > 0: return 0

        line1, line2 = line2, line1
        
    return 1


line1 = map(int, input().split())
line2 = map(int, input().split())

print(sol(line1, line2))
