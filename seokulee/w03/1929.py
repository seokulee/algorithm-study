import sys
import math

N, M = map(int, sys.stdin.readline().split())

arr = [True for _ in range(M+1)] # 0, 1, 2 ... M (0, 1 제외해야함)
arr[0] = arr[1] = False # @@@@@@@@@@@@@@

# isprime을 만들어 일일이 확인하는 거 보다 6배정도 빠름.
for i in range(2, int(math.sqrt(M) + 1)):
    if arr[i]:
        j = 2
        while i * j <= M:
            arr[i * j] = False
            j += 1

# for i in range(N, M+1):
#     if arr[i]:
#         print(i)

# 살짝 더 빠름
print('\n'.join(str(i) for i in range(N, M+1) if arr[i]))
