def sol(data):
    p1, p2, i1, i2 = [0] * 4 # p는 과일값, i는 인덱스 dp
    maxi = 0

    for i, v in enumerate(data):
        if v == p2: 
            p1, p2 = v, p1
            i1 = i
        
        # v가 p1, p2가 아니면
        elif v != p1:
            p1, p2 = v, p1
            i1, i2 = i, i1

        if (leng := i - i2 + 1) > maxi: maxi = leng

    return maxi

print(sol(map(int, open(0).read().split()[1:])))
