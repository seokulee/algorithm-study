import sys
import math



readline = sys.stdin.readline


def num_of_stored(n):
    a = math.floor(math.log2(n))
    b = n - (2 ** a)

    return a*(2**a) + (a + 2)*b


def find(arr, n, k):
    if num_of_stored(n) < k:
        return -1

    return sub(arr, n, k)


def sub(arr, n, k):
    half = (n+1)//2
    left = num_of_stored(half)
    if left >= k:
        return sub(arr[:half], half, k)
    
    right = left + num_of_stored(n-half)
    if right >= k:
        return sub(arr[half:], n-half, k-left)
    
    return sorted(arr)[k - right - 1]

    
N, K = map(int, readline().strip().split())
arr = list(map(int, readline().strip().split()))

print(find(arr, N, K))
