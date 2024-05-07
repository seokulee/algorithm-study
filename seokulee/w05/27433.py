import sys
import time
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())

def factorial(N: int):
    if N <= 1:
        return 1

    return N * factorial(N-1)

# test 1 : recursive
s = time.time()
factorial(N)
e = time.time()
print("recursive factorial", e - s)

# test 2 : math lib
import math
s = time.time()
math.factorial(N)
e = time.time()
print("math lib", e - s)

# test 3 : loop
result = 1
s = time.time()
for i in range(2, N+1):
    result *= i
e = time.time()
# print(result)
print("loop factorial", e - s)

# test 1,2,3의 결과는 다 같게 나옴.
# 시간은 N이 1000일 때,
# recursive factorial 0.0011398792266845703
# math lib            8.177757263183594e-05
# loop factorial      0.00055694580078125
# library활용이 압도적으로 성능이 좋고, 다음 loop, recursive 순임.
# 재귀는 함수 호출 및 스택 조작에 오버헤드가 발생한다.
# 가독성은 재귀가 좋을 수 있으나 성능면에선 반복.
