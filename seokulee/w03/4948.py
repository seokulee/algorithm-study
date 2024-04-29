import sys
import math

n_max = 123456

arr = [True for _ in range(n_max * 2 + 1)]
arr[0] = arr[1] = False

for i in range(2, int(math.sqrt(n_max * 2) + 1)):
    if arr[i]:
        j = 2
        while i * j <= n_max * 2:
            arr[i * j] = False
            j += 1

while(True):
    input = int(sys.stdin.readline())
    if  input == 0:
        break

    print(sum([1 for i in range(input + 1, input * 2 + 1) if arr[i]]))
