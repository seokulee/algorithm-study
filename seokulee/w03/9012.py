import sys

T = int(sys.stdin.readline())

stack = []
for _ in range(T):
    PS = sys.stdin.readline().rstrip()
    for c in PS:
        if c == '(':
            stack.append('(')
        else:
            try:
                stack.pop()
            except:
                stack.append(0)
                break
    if len(stack):
        print("NO")
    else:
        print("YES")
    stack.clear()

# 예전 버전 속도가 미세하게 빠름

# N = int(sys.stdin.readline())

# for _ in range(N):
#     input = sys.stdin.readline().rstrip()
#     valid = 0
#     for c in input:
#         if c == '(':
#             valid += 1
#         elif c == ')':
#             valid -= 1
#         if valid < 0:
#             break
#     print('YES' if valid == 0 else 'NO')
