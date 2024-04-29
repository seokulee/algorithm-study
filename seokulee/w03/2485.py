import sys
import math

N = int(sys.stdin.readline())

arr = list()
x = int(sys.stdin.readline())
for _ in range(N-1):
    y = int(sys.stdin.readline())
    arr.append(y-x)
    x = y

gcd = math.gcd(*arr)

result = 0
for i in range(len(arr)):
    result += (arr[i] // gcd - 1)

print(result)
