from bisect import bisect_left



def find(arr):
    stack = [0]
    for v in arr:
        if v > stack[-1]: 
            stack.append(v)
        else: 
            stack[bisect_left(stack, v)] = v
    
    return len(stack) - 1


input()
arr = tuple(map(int, input().split()))

print(find(arr))
