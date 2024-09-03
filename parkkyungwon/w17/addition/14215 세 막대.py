sides = sorted(map(int, input().split()))

def sol():
    a = sides[0] + sides[1]

    if sides[2] >= a: return 2*a - 1
    else: return sides[2] + a

print(sol())
