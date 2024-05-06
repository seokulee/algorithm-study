import sys

stack = list()

while(True):
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break

    for c in line:
        if c == '(':
            stack.append(c)
        elif c == '[':
            stack.append(c)
        elif c == ')':
            try:
                if stack.pop() != '(':
                    stack.append(0)
                    break
            except:
                stack.append(0)
                break
        elif c == ']':
            try:
                if stack.pop() != '[':
                    stack.append(0)
                    break
            except:
                stack.append(0)
                break

    if len(stack):
        print('no')
    else:
        print('yes')
    stack.clear()
