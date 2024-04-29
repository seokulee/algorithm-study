import sys
import math

N = int(sys.stdin.readline())

def isprime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False

    return True

for _ in range(N):
    num = int(sys.stdin.readline())
    if num <= 2: # 예외처리 수정
        print(2)
        continue
    while (not isprime(num)):
        num += 1
    print(num)
