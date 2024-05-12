N, B = map(int, input().split())

total = ''
while N:
    num = N % B
    num = chr(num + 55) if 9 < num else str(num)

    total = num + total
    N //= B

print(total)
