def sol(inte, a, b):
    ### 주어진 문제는 이미 적분된 값을 제공해줘서, a인덱스와 b인덱스 사이의 합이 곧 답이다.

    total = 0
    ### 주기의 길이와 1 주기의 전체 합을 구한다
    l, sums = len(inte), sum(inte)

    ### a와 b의 차이가 1 주기보다 크다면 그만큼 total에 1주기 전체 합을 더한다.
    total += ((b - a) // l) * sums
    ### a와 b의 절대값이 1 주기 크기보다 작게 만든다.
    a, b = a % l, b % l

    ### 나머지를 더해준다.
    if a > b:
        total += sum(inte[a:])
        total += sum(inte[:b])
    else:
        total += sum(inte[a:b])
    
    return total


input()
inte = (*map(int, input().split()), )
a, b = map(int, input().split())

print(sol(inte, a, b))
