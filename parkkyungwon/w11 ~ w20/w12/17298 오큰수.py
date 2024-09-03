def sol(arr):
    answer = [-1] * len(arr)
    stack = []
    
    # 배열의 인덱스를 stack 넣고 빼서 비교
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            answer[stack.pop()] = arr[i]
            
        stack.append(i)
        
    return ' '.join(map(str, answer))


input()
arr = (*map(int, input().split()), )

print(sol(arr))
