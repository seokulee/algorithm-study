_ = input()

A = set(map(int, input().split()))
B = set(map(int, input().split()))

C = A.difference(B)
D = B.difference(A)
print(len(C.union(D)))
