import sys



readline = sys.stdin.readline

n = int(readline())

stack = []
for _ in range(n):
    c = int(readline())

    if c == 0:
        stack.pop()
    
    else:
        stack.append(c)

print(sum(stack))
