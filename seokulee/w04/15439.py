import sys
from itertools import permutations

N = int(sys.stdin.readline())

print(len(list(permutations(range(N), 2))))

# 지난 번 했던거 ... 더 쉽게 했었네
# permutation의 list는 필요없고 갯수만 필요한거니깐 수학적으로 계산해서 print
# N = int(sys.stdin.readline())

# print(N ** 2 - N)
