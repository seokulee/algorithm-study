import sys

def solution(A, B, C):
    if B == 1:
        return A % C
    elif B % 2 == 0:
        return (solution(A, B//2, C) ** 2) % C
    else:
        return (solution(A, B//2, C) ** 2 * A) % C


A, B, C = map(int, sys.stdin.readline().split())
print(solution(A, B, C))

# remainder = set()
# num = A
# while True:
#     if num % C in remainder:
#         break
#     remainder.add(num % C)
#
#     num *= A
# remainder = list(remainder)
# print(remainder[B % len(remainder)])
