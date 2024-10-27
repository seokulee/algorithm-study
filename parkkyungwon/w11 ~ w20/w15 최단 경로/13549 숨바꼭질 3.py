import heapq



def sol(n, k):
    # 형과 동생의 위치가 같으면 0
    if n == k:
        return 0

    # 형의 위치가 동생 위치 보다 크면, 1칸씩 뒤로가는 경우밖에 존재하지 않아서 n-k
    elif n > k:
        return n - k
    
    maxi = k + 1
    hist = [float('inf') for _ in range(maxi + 1)]
    vertexes = [(0, n)]
    
    while vertexes:
        second, position = heapq.heappop(vertexes)

        if position == k:
            break

        if second > hist[position]:
            continue

        # 형의 위치가 0이 아닐 때만 순간이동 계산
        if position:
            i = position * 2
            while i <= maxi:
                if second < hist[i]:
                    hist[i] = second
                    heapq.heappush(vertexes, (second, i))
                
                i *= 2

        second2 = second + 1
        for i in position-1, position+1:
            if  0 < i <= maxi and second2 < hist[i]:
                hist[i] = second2
                heapq.heappush(vertexes, (second2, i))
    
    return hist[k]


N, K = map(int, input().split())
print(sol(N, K))
