import sys
import math

n_max = 1_000_000

arr = [True for _ in range(n_max + 1)]
arr[0] = arr[1] = False

for i in range(2, int(math.sqrt(n_max) + 1)):
    if arr[i]:
        # 수정
        for j in range(i*i, n_max + 1, i):
            arr[j] = False

arr_prime = [i for i in range(n_max) if arr[i]]

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    count = 0
    left = 0
    right = len(arr_prime) - 1
    # C2 :
    while right >= left:
        if arr_prime[left] + arr_prime[right] == N:
            count += 1
            left += 1
            right -= 1
        elif arr_prime[left] + arr_prime[right] < N:
            left += 1
        else:
            right -= 1
    # C1 : 2676ms (너무 오래걸림)
    # for i in range(2, N//2 + 1):
    #     if arr[i] and arr[N-i]:
    #         count += 1

    print(count)
