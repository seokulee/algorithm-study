import itertools



def sol(data):
    # x1 = 0, y1 = m1
    # x2 = sqrt(2)/2 * m2 = y2
    # x3 = m3, y3 = 0
    #
    # if 0 < ad - bc : 반시계
    # ad - bc
    # = ((x2 - x1) * (y3 - y2)) - ((y2 - y1) * (x3 - x2))
    # = ((x2 - 0) * (0 - y2)) - ((y2 - m1) * (m3 - x2))
    # = -(x2 * y2) - ((y2 - m1) * (m3 - x2))
    # = -x2y2 - (y2m3 - m1m3 - x2y2 + x2m1)
    # = - y2m3 + m1m3 - x2m1
    # = - sqrt(2)/2 * m2 * m3 + m1m3 - sqrt(2)/2 * m2 * m1
    # = - sqrt(2)/2 * m2(m3 + m1) + m1m3
    #
    # if 0 < - sqrt(2)/2 * m2(m3 + m1) + m1m3 : 반시계
    # -m1m3 < - sqrt(2)/2 * m2(m3 + m1)
    # m1m3 > sqrt(2)/2 * m2(m3 + m1)
    # sqrt(2) * m1m3 > m2(m1 + m3)
    # 2*(m1m3)^2 > (m2(m1 + m3))^2
    # 2*(m1m3)^2 - (m2(m1 + m3))^2 > 0

    count = 0
    s, data = (data[0], ), data[1:]

    for arr in itertools.permutations(data, 7):
        arr += s

        for i in range(-2, 6):
            n1, n2, n3 = arr[i], arr[i+1], arr[i+2]

            if 2*(n1*n3)**2 - (n2*(n1 + n3))**2 > 0: break
        
        else:
            count +=1
    
    # s를 기준으로 회전된 경우를 고려해서 8을 곱해준다
    return 8*count

data = tuple(map(int, input().split()))

print(sol(data))
