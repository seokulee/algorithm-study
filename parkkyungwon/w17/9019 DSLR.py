import sys


def sol(start, end, path):
    dp = [None] * L
    dp[start] = 0

    # bfs
    def f():
        queue = [start, None]
        count = 1
        
        for a in queue:
            if a == None:
                if queue[-1] == None: break

                queue.append(None)
                count += 1
                continue

            for b in path[a]:
                if dp[b] != None: continue

                queue.append(b)
                dp[b] = count

                if b == end: return count
                
    # 최단 경로 역추적
    count = f()
    answer = [None] * (count)
    a = end
    for i in range(count-1, -1, -1):
        for char, b in zip(('S', 'L', 'R', 'D', 'D'), (0 if a == 9999 else a+1, a//10 + 1000*a%L, 10*a%L + a//1000, a//2, a//2 + 5000)):
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

    sys.stdout.write(sol(A, B, path) + '\n')
