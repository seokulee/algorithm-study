# 투 포인터, bfs를 사용
# def forward(i):
#     if i: yield i-1

#     for a in i+1, 2*i:
#         if a >= L: return
#         yield a


# def backward(i):
#     if i: yield i-1

#     a = i + 1
#     if a < L: yield a

#     if i % 2 == 0: yield i//2


# def sol(n, k):
#     if n == k:
#         return 0, [n]
    
#     if n > k:
#         return n-k, [i for i in range(n, k-1, -1)]

#     dp = [None] * (L)

#     # bfs
#     def f():
#         dp[n] = 0
#         dp[k] = -1
#         queue_for = [n]
#         queue_bac = [k]

#         # 시작점과 끝점에서 동시에 출발
#         for s_count, e_count in zip(range(1, L), range(-2, -L, -1)):
#             for queue, gen, count, is_for in zip((queue_for, queue_bac), (forward, backward), (s_count, e_count), (True, False)):
#                 queue_tmp = []

#                 for curr_i in queue:
#                     for next_i in gen(curr_i):
#                         if dp[next_i] != None:
#                             if is_for:
#                                 if dp[next_i] < 0: return s_count-1, e_count+2, next_i
#                             else: 
#                                 if dp[next_i] > 0: return s_count-1, e_count+1, next_i
                            
#                             continue
                        
#                         dp[next_i] = count
#                         queue_tmp.append(next_i)

#                 if is_for: queue_for = queue_tmp
#                 else: queue_bac = queue_tmp

#     # 최단 경로 역추적
#     s_count, e_count, m = f()
#     leng = s_count - e_count + 2
#     answer = [None] * leng
#     answer[leng//2] = m

#     for s, e, op, gen in zip((s_count, e_count), (-1, 0), (-1, 1), (backward, forward)):
#         a = m
#         for i in range(s, e, op):
#             for b in gen(a):
#                 if dp[b] == i:
#                     answer[i] = b
#                     a = b
#                     break
    
#     return len(answer) - 1, answer


# N, K = map(int, input().split())
# L = K + 2

# leng, answer = sol(N, K)
# print(leng)
# print(*answer)




def sol(n, k):
    if n == k:
        return 0, [n]
    
    if n > k:
        return n-k, [i for i in range(n, k-1, -1)]

    dp = [0] * (k+2)
    dp[n] = -1
    L = k + 1

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
