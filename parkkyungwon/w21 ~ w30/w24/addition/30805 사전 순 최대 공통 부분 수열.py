def sol(a, b):
    answer = []

    while a and b:
        sa, sb = iter(sorted(set(a), reverse=True)), iter(sorted(set(b), reverse=True))
        ia, ib = next(sa), next(sb)

        try:
            while ia != ib:
                if ia > ib: ia = next(sa)
                else: ib = next(sb)

        except StopIteration: break

        answer.append(ia)
        
        a = a[a.index(ia) + 1:]
        b = b[b.index(ia) + 1:]

    return len(answer), answer


input()
A = tuple(map(int, input().split()))
input()
B = tuple(map(int, input().split()))

leng, answer = sol(A, B)

print(leng)
print(*answer)
