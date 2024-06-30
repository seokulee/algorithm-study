import sys

string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

stack = list()
for s in string:
    stack.append(s)
    if len(stack) >= len(bomb):
        if ''.join(stack[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
