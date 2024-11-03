import sys



def sol(arr):
    stack = []
    t = 0

    for v in arr:
        # 스택의 뒤에서 부터, arr에서 뽑은 값보다 작은 값들을 지운다.
        # 스택은 내림차순 형태를 띤다
        while stack and v > stack[-1][0]:
            t += stack[-1][1]
            del stack[-1]

        # 스택에 마지막 값이 추가하려는 값과 같으면 추가하지 않고 중복 횟수를 늘린다
        if stack and stack[-1][0] == v:
            t += stack[-1][1]
            stack[-1][1] += 1

            if len(stack) > 1:
                t += 1

        else:
            if stack:
                t += 1
                
            # 스택에 값을 추가할 땐 [값, 개수]로 개수는 똑같은 값이 몇번 있는지 나타내는 중복 횟수를 저장한다.
            stack.append([v, 1])

    return t


N = int(input())
arr = [int(sys.stdin.readline()) for _ in range(N)]

print(sol(arr))
