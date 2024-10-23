def sol(a, b):
    count = 1

    while a < b:
        count += 1

        if b % 2 == 0: b //= 2
        elif b % 10 == 1: b = (b - 1) // 10
        else: break
    
    return count if a == b else -1


A, B = map(int, input().split())

print(sol(A, B))
