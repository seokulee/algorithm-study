import sys

stack = list()
K = int(sys.stdin.readline())

for _ in range(K):
    m = sys.stdin.readline().rstrip()
    if m == '0':
        stack.pop()
    else:
        stack.append(int(m))

print(sum(stack))
