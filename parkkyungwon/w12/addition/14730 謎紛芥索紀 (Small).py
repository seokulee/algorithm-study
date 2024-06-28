N = int(input())
# f'(1)의 값만 출력하면 되서 항의 계수와 차수를 곱한 것들을 다 더해주면 된다.
r = sum(a * b for a, b in (map(int, input().split()) for _ in range(N)))

print(r)
