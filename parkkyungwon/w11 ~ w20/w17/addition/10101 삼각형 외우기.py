angles = [int(input()) for _ in range(3)]

def sol():
    if sum(angles) != 180: return 'Error'

    a = len(set(angles))

    if a == 1: return 'Equilateral'
    elif a == 2: return 'Isosceles'
    else: return 'Scalene'
    
print(sol())
    