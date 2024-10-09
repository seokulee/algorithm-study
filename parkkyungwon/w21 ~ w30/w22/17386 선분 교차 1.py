x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

answer = 0
for _ in range(2):
    arr = []
    tx, ty = (x1 - x2), (y1 - y2)
    for v1x, v1y in ((tx, ty), (-tx, -ty)):
        for xt, yt in zip((x3, x4), (y3, y4)):
            v2x, v2y = (x2 - xt), (y2 - yt)
            arr.append((v1x*v2y - v1y*v2x) > 0)

    x1, y1, x2, y2, x3, y3, x4, y4 = x3, y3, x4, y4, x1, y1, x2, y2

    if (arr[0] ^ arr[1]) & (arr[2] ^ arr[3]) & (arr[0] ^ arr[2]): continue
    else: break

else:
    answer = 1

print(answer)
