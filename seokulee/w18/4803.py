import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def findCycle(start):
    isCycle = False
    q = deque()
    q.append(start)

    while q:
        current = q.popleft()
        if visited[current]:
            isCycle = True

        visited[current] = 1

        for node in graph[current]:
            if visited[node] == 0:
                q.append(node)

    return isCycle

n, m = map(int, input().split())
case = 1

while n != 0 or m != 0:
    graph = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    count = 0

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for node in range(1, n+1):
        if not visited[node]:
            if not findCycle(node):
                count += 1

    if count == 0:
        print(f'Case {case}: No trees.')
    elif count == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {count} trees.')

    case += 1
    n, m = map(int, input().split())
