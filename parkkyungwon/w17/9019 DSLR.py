import sys



def sol(start, end):
    dp = [0] * L

    def bfs():
        dp[start] = 1
        dp[end] = -1
        queue_for = [start]
        queue_rev = [end]

        for i, j in zip(range(2, 5000), range(-2, -5000, -1)):
            queue2_for = []
            for q in queue_for:
                for k in path_for[q]:
                    if not dp[k]:
                        dp[k] = i
                        queue2_for.append(k)
                    
                    elif dp[k] < 0: return i-1, j+2, k               
            
            queue_for = queue2_for

            queue2_rev = []
            for q in queue_rev:
                for k in path_rev[q]:
                    if not dp[k]:
                        dp[k] = j
                        queue2_rev.append(k)

                    elif dp[k] > 0: return i-1, j+1, k       
            
            queue_rev = queue2_rev

    i, j, k = bfs()
    # 최단 경로 역추적
    answer = [None] * (i-j)

    a = k
    for b in range(i, 0, -1):
        for char, c in zip(('S', 'L', 'R', 'D', 'D'), path_rev[a]):
            if dp[c] == b:
                answer[b-1] = char
                a = c
                break
    
    a = k
    for b in range(j, 0):
        for char, c in zip(('S', 'L', 'R', 'D'), path_for[a]):
            if dp[c] == b:
                answer[b] = char
                a = c
                break
    
    return ''.join(answer)


readline = sys.stdin.readline
T = int(readline())
L = 10000
path_for = [(i-1 if i else 9999, 10*i%L + i//1000, i//10 + 1000*i%L, 2*i%L) for i in range(L)]
path_rev = [(0 if i == 9999 else i+1, i//10 + 1000*i%L, 10*i%L + i//1000, j := i//2, j+5000)
            if i % 2 == 0 else 
            (0 if i == 9999 else i+1, i//10 + 1000*i%L, 10*i%L + i//1000) for i in range(L)]

for _ in range(T):
    A, B = map(int, readline().split())

    sys.stdout.write(sol(A, B) + '\n')
