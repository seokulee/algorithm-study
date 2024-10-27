import bisect



def sol(arr, goal):
    L = len(arr) + 1

    # 0부터 i까지 합을 구한다
    sums = [0] * L
    for i in range(L - 1):
        sums[i+1] = sums[i] + arr[i]

    # 가장 왼쪽 요소를 포함하고, goal을 만족하고, 가장 짧은 수열을 찾는다
    s = 0
    e = bisect.bisect_left(sums, goal)
    if e == L:
        return 0

    # s를 오른쪽으로 1칸 이동 하고 수열을 계산한다.
    # 계산 결과가 goal을 만족하면, 현재까지 발경한 가장 짧은 수열
    # 계산 결과가 goal을 만족하지 않으면, 수열을 길이를 유지하기 위해 e도 오른쪽으로 1칸 이동
    while e < L:
        s += 1
        if sums[e] - sums[s] < goal:
            e += 1
        
    return e - s


S = int(input().split()[1])
arr = tuple(map(int, input().split()))

print(sol(arr, S))
