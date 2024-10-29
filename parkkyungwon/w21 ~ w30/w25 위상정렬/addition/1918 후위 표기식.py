def parse(arr):
    stack = []
    answer = []

    for v in map(ord, arr):
        if 64 < v < 91:
            answer.append(v)
        
        elif v == 40: 
            stack.append(v)

        elif v == 41:
            while (v2 := stack.pop()) != 40:
                answer.append(v2)
        
        elif v == 43 or v == 45:
            while stack and stack[-1] != 40:
                answer.append(stack.pop())
            
            stack.append(v)
        
        else:
            while stack and (stack[-1] == 42 or stack[-1] == 47):
                answer.append(stack.pop())

            stack.append(v)
    
    answer += stack[::-1]

    return ''.join(map(chr, answer))


print(parse(input()))
