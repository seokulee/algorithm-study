import bisect



def sol(arr):
    L = len(arr)
    greed = [arr[0]]
    dp = [0] * L

    for i in range(L):
        v = arr[i]
        if greed[-1] < v:
            j = len(greed)
            greed.append(v)
        
        else:
            j = bisect.bisect_left(greed, v)
            greed[j] = v
        
        # i번 째 수가 greed에 추가된 위치를 dp에 저장
        dp[i] = j
    
    # 그리디 변수를 정답 수열로 변경
    count = len(greed) - 1
    prev = float('inf')

    for i in range(L-1, -1, -1):
        if count == dp[i] and arr[i] < prev:
            greed[count] = arr[i]
            prev = arr[i]
            count -= 1

    return len(greed), greed


input()
arr = tuple(map(int, input().split()))

leng, answer = sol(arr)

print(leng)
print(*answer)
