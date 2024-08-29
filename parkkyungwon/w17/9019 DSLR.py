import sys



def sol(start, end):
    dp = [10000] * L

    def bfs():
        dp[start] = 0
        queue = [start]
        for i in queue:
            c = dp[i] + 1

            for j in path[i]:
                if dp[j] > c:
                    dp[j] = c

                    if j == end: return
                    queue.append(j)

    bfs()
    # 최단 경로 역추적
    count = dp[end]
    answer = [None] * (count)
    a = end
    for i in range(count-1, -1, -1):
        for char, b in zip(('S', 'L', 'R', 'D', 'D'), (0 if a == 9999 else a+1, a//10 + 1000*a%L, 10*a%L + a//1000, k := a//2, k + 5000)):
            if dp[b] == i:
                answer[i] = char
                a = b
                break
    
    return ''.join(answer)


readline = sys.stdin.readline
T = int(readline())
L = 10000
path = tuple((2*i%L, i-1 if i else 9999, 10*i%L + i//1000, i//10 + 1000*i%L) for i in range(L))

for _ in range(T):
    A, B = map(int, readline().split())

    sys.stdout.write(sol(A, B) + '\n')
