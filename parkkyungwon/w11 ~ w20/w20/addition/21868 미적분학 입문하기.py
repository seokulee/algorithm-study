numer, denom = map(int, input().split())
xcoef, const = map(int, input().split())
x0 = int(input())

L = xcoef * x0 + const
print(L)

if xcoef:
    denom = denom * abs(xcoef)
    answer = (numer, denom)
else:
    answer = (0, 0)

print(*answer)
