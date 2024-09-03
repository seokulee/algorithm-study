def forward(i):
    for a in i+1, 2*i, 3*i:
        if a >= L: return
        yield a


def backward(i):
    if i % 3 == 0: yield i // 3
    if i % 2 == 0: yield i // 2
    yield i - 1


def sol(n):
    if n == 1:
        return 0, [1]

    dp = [None] * (L)

    # 투 포인터, bfs
    def search():
        dp[1], dp[n] = 0, -1
        queue_for, queue_bac = [1], [n]

        for s_side, e_side in zip(range(1, L), range(-2, -L, -1)):
            for queue, gen, is_for in zip((queue_for, queue_bac), (forward, backward), (True, False)):
                queue_tem = []

                for q in queue:
                    for k in gen(q):
                        if dp[k] == None:
                            dp[k] = s_side if is_for else e_side
                            queue_tem.append(k)
                        
                        elif is_for:
                            if dp[k] < 0: return s_side-1, e_side+2, k
                        else:
                            if dp[k] >= 0: return s_side-1, e_side+1, k
                
                if is_for: queue_for = queue_tem
                else: queue_bac = queue_tem
    
    s_side, e_side, m = search()
    
    # 중앙에서 출발지와 도착지로 경로를 찾는다
    leng = s_side - e_side + 2
    answer = [None] * leng
    answer[leng//2] = m

    for s, e, op, gen in zip((s_side, e_side), (-1, 0), (-1, 1), (backward, forward)):
        a = m
        for i in range(s, e, op):
            for j in gen(a):
                if dp[j] == i:
                    answer[i] = j
                    a = j
                    break

    return leng-1, answer[::-1]
        

N = int(input())
L = N + 1

leng, path = sol(N)

print(leng)
print(*path)
