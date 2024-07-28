import sys



def sol(arr):
    area = 0

    def f(s, e):
        nonlocal area

        # 시작과 끝 사이의 길이를 계산해서 2개 이하면 간단히 넓이를 계산한다.
        L = e - s
        if L == 0: 
            if area < arr[s]:
                area = arr[s]
            return
        
        elif L == 1:
            area = max(area, arr[s], arr[e], min(arr[s], arr[e]) * 2)
            return

        mid = (s+e)//2

        f(s, mid-1)
        f(mid+1, e) 

        l = r = mid
        h = arr[mid]
        if h > area:
            area = h

        # 현재 중간지점에서 왼쪽을 확인하고 더 큰 쪽으로 범위를 넓혀가면서, 
        # 동시에 높이가 가장 낮은 블럭을 기준으로 넓이를 계산.
        # max나 min을 반복문 안에 사용하면 속도가 많이 느려저서 if로 대체
        while l > s and r < e:
            if arr[l-1] < arr[r+1]:
                r += 1
                t = arr[r]

            else:
                l -= 1
                t = arr[l]

            if t < h:
                h = t

            t = h * (r-l+1)
            if t > area:
                area = t
            
        for a in range(r+1, e+1):
            if arr[a] < h:
                h = arr[a]
            
            t = h * (a-s+1)
            if t > area:
                area = t

        for a in range(l-1, s-1, -1):
            if arr[a] < h:
                h = arr[a]
            
            t = h * (e-a+1)
            if t > area:
                area = t


    f(0, len(arr)-1)

    return area


N = int(input())
arr = tuple(int(sys.stdin.readline()) for _ in range(N))

print(sol(arr))
