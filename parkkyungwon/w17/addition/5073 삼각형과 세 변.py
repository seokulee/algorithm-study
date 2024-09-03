while 1:
    sides = tuple(map(int, input().split()))

    if not all(sides): break

    def sol():
        if 2*max(sides) >= sum(sides): return 'Invalid'

        a = len(set(sides))

        if a == 1: return 'Equilateral'
        elif a == 2: return 'Isosceles'
        else: return 'Scalene'
        
    print(sol())
