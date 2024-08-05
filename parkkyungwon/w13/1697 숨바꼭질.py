def sol(n, k):
    # 형과 동생의 위치가 같으면 0
    if n == k:
        return 0

    # 형의 위치가 동생 위치 보다 크면, 1칸씩 뒤로가는 경우밖에 존재하지 않아서 n-k
    elif n > k:
        return n - k
    
    hist = {n, }
    # -1은 depth를 표시하기위함
    next_spot = [n, -1]
    count = 0
    maxi = k + 1
    
    for i in next_spot:
        if i == k:
            break
        elif i == -1:
            count += 1
            next_spot.append(-1)
            continue
        
        for j in i-1, i+1, i*2:
            if j in hist or j > maxi or j < 0:
                continue

            next_spot.append(j)
            hist.add(j)
    
    return count


N, K = map(int, input().split())

print(sol(N, K))
