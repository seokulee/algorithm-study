N, B = input().split()
B = int(B)

digit = len(N) - 1
total = 0
for n in N:
    num = int(n) if n in "0123456789" else (ord(n) - 55)
    total += num * (B**digit)
    digit -= 1

print(total)
