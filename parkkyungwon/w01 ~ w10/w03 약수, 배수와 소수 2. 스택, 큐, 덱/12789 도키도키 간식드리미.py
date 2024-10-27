def pop(n, stack1, stack2):
    if len(stack1) and stack1[0] == n:
        stack1.pop(0)
        return True

    elif len(stack2) and stack2[-1] == n:
        stack2.pop()
        return True
    
    else:
        return False

def shift(stack1, stack2):
    if len(stack1):
        stack2.append(stack1.pop(0))
        return True
    
    else:
        return False

def check(n, stack1, stack2):
    while not pop(n, stack1, stack2):
        if not shift(stack1, stack2):
            return False

    return True


n = int(input())
stack1 = list(map(int, input().split()))
stack2 = []

for i in range(1, n+1):
    if not check(i, stack1, stack2):
        print('Sad')
        break

else:
    print('Nice')
    