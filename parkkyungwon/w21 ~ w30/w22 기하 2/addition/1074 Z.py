import math 



def z(i):
    count = 0

    while i:
        v = int(math.log2(i))
        count += 4**v
        i -= 2**v
    
    return count


N, r, c = map(int, input().split())

print(z(r) * 2 + z(c))
