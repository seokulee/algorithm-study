import sys
from collections import deque
sys.setrecursionlimit(10**6)
visited = [False] * 100001

def bfs(N, K):
    visited[N] = True
    q = deque([(N, 0)])

    while q:
        a, b = q.popleft()
        if a == K:
            print(b)
            break
        if a - 1 >= 0 and not visited[a - 1]:
            q.append((a - 1, b + 1))
            visited[a - 1] = True
        if a + 1 <= 100000 and not visited[a + 1]:
            q.append((a + 1, b + 1))
            visited[a + 1] = True
        if a * 2 <= 100000 and not visited[a * 2]:
            q.append((a * 2, b + 1))
            visited[a * 2] = True

N, K = map(int, sys.stdin.readline().split())
bfs(N, K)
