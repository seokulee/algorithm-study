def sol(c, abn):
    l = len(c)
    a, b, n = abn
    dx = (b-a) / n

    def F(x):
        return sum(c[i] / (ex := l-i) * (x ** ex) for i in range(l))
    
    actural_value = F(b) - F(a)

    def f(x):
        return sum(c[i] * (x ** (l-i-1)) for i in range(l))

    def approx(epsil):
        t = a + epsil
        return sum(f(t + dx*i) * dx for i in range(n))
    
    x1, x2 = approx(0), approx(dx)
    if not(x1 <= actural_value <= x2):
        return -1

    return (actural_value - x1) / c[0]
    

def sol2(abn):
    ### 최고차수가 항상 1이다. 그래프를 그려보면 항상 직선이다.
    ### 문제의 근사 방식은 좌 리만합이다. 주어진 다항식이 항상 직선이어서, 오차는 정확한 삼각형으로 그려진다.
    ### 좌 리만합을 중간 리만합으로 변경하면 오차가 없어진다. a에서 dx의 절반 만큼 움직이면, 좌 리만합이 중간 리만합으로 변경된다.
    a, b, n = abn
    epsil = (b-a) / n / 2

    return epsil


input()
input()
abn = map(int, input().split())

print(sol2(abn))
