N = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

arr = [B[i] for i in range(N) if A[i] == 0]
result = arr[::-1] + C

for r in result[:M]:
    print(r, end=' ')