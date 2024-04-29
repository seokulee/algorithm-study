import sys



def is_vps(string):
    stack = []
    for s in string:
        if s in '({[':
            stack.append(s)

        elif s in ')}]':
            if len(stack) == 0:
                break

            t = stack.pop()
            if s == ')' and t != '(':
                break

            elif s == '}' and t != '{':
                break

            elif s == ']' and t != '[':
                break
    
    else:
        if len(stack) == 0:
            return True
    
    return False


readline = sys.stdin.readline
writeline = sys.stdout.writelines

while True:
    string = readline().rstrip()

    if len(string) == 1 and string[0] == '.':
        break

    if is_vps(string):
        writeline('yes\n')

    else:
        writeline('no\n')
        