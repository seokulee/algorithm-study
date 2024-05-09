from itertools import permutations



def insert_op():
    global num, op
    tmax = -1e10
    tmin = 1e10

    for case in op:
        t = num[0]
        for a, b in zip(num[1:], case):
            if b == 0:
                t += a
            elif b == 1:
                t -= a
            elif b == 2:
                t *= a
            else:
                if t < 0:
                    t = -(-t // a)
                else:
                    t //= a


        tmax = max(tmax, t)
        tmin = min(tmin, t)
    
    return tmax, tmin


input()
num = tuple(map(int, input().split()))
op = []
for x, y in enumerate(map(int, input().split())):
    op += [x] * y

op = set(permutations(op))

tmax, tmin = insert_op()

print(tmax, tmin, sep='\n')
