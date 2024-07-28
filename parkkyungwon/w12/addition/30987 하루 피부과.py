x1, x2 = map(int, input().split())
coeff = (*map(int, input().split()), )

coeff2 = (coeff[0], coeff[1] - coeff[3], coeff[2] - coeff[4])

### 원시함수
def F(coeff, x):
    l = len(coeff)
    return sum(coeff[i] * (x ** (d := l-i) / d) for i in range(l))

answer = F(coeff2, x2) - F(coeff2, x1)

print(int(answer))
