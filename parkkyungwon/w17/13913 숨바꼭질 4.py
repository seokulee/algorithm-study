def sol(n, k):
    if n == k:
        return 0, [n]
    
    if n > k:
        return n-k, [i for i in range(n, k-1, -1)]

    dp = [0] * (k+2)
    dp[n] = -1
    L = k + 1

    # bfs
    def f():
        queue = [n, -1]
        count = 1
        
        for a in queue:
            if a == -1:
                if queue[-1] == -1: break

                queue.append(-1)
                count += 1
                continue

            for b in a-1, a+1, 2*a:
                if b > L or b < 0 or dp[b]: continue

                queue.append(b)
                dp[b] = count
                
                if b == k: return count

    # 최단 경로 역추적
    count = f()
    answer = [n] + [0] * (count-1) + [k]
    a = k
    for i in range(count-1, 0, -1):
        for b in a-1, a+1, a//2:
            if b <= L and b >= 0 and dp[b] == i:
                answer[i] = b
                a = b
                break
    
    return len(answer) - 1, answer


N, K = map(int, input().split())

leng, answer = sol(N, K)
print(leng)
print(*answer)
