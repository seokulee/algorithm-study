def sol(arr):
    # 오큰수 코드에 count만 추가
    # count에 배열에서 나타나는 수를 카운트
    # 처음엔 default dict를 사용했지만 무식하게 list를 사용하는게 메모리와 속도, 둘 다 좋다
    count = [0] * 1000001
    for a in arr:
        count[a] += 1

    answer = [-1] * len(arr)
    stack = []
    
    # 배열의 인덱스를 stack 넣고 빼서 비교
    for i in range(len(arr)):
        while stack and count[arr[i]] > count[arr[stack[-1]]]:
            answer[stack.pop()] = arr[i]
            
        stack.append(i)
        
    return ' '.join(map(str, answer))


input()
arr = (*map(int, input().split()), )

print(sol(arr))
