arr = tuple(map(int, open(0).read().split()))
N = arr[0]
stack = []
answer = []
count = 1

for a in arr[1:]:
    while a >= count:
        stack.append(count)
        count += 1
        answer.append('+')

    if a != stack[-1]: 
        print('NO')
        break
    
    stack.pop()
    answer.append('-')

else:
    print(*answer, sep='\n')
