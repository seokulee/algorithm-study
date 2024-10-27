N = int(input())
num = 1
z_count = 0

for i in range(1, N+1):
    num *= i
    
    while num % 10 == 0:
        num //= 10
        z_count += 1
    
    num %= 10000

print(z_count)
