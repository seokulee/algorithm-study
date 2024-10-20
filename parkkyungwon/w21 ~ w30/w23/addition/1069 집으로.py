def sol(data):
    x, y, d, t = data

    dist = (x**2 + y**2)**(0.5)

    if d < t: return dist

    time = 0

    if dist > 2*d:
        q = dist//d - 1
        dist -= q*d
        time += q*t
    
    time += min(dist, 2*t, t + abs(d - dist))

    return time


data = map(int, input().split())

print(sol(data))
