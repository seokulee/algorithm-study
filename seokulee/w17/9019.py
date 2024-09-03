import sys
from collections import deque

T = int(sys.stdin.readline())

def bfs(A, B):
    if A == B:
        return ""

    q = deque([A])
    visited[A] = 1
    parent = [-1] * 10000
    move = [''] * 10000

    while q:
        x = q.popleft()

        D = (2 * x) % 10000
        S = (x - 1) if x != 0 else 9999
        L = (x % 1000) * 10 + (x // 1000)
        R = (x % 10) * 1000 + (x // 10)

        nx = [('D', D), ('S', S), ('L', L), ('R', R)]

        for d, num in nx:
            if not visited[num]:
                visited[num] = 1
                parent[num] = x
                move[num] = d
                if num == B:
                    return reconstruct_path(A, B, parent, move)
                q.append(num)

def reconstruct_path(A, B, parent, move):
    path = []
    current = B
    while current != A:
        path.append(move[current])
        current = parent[current]
    return ''.join(reversed(path))

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())

    visited = [0] * 10000
    print(bfs(A, B))

# pypy3 -> 212864kb, 4400ms
# import sys
# from collections import deque

# T = int(sys.stdin.readline())

# def bfs(A, B):
#     if A == B:
#         return ""

#     q = deque([A])
#     graph[A] = 1

#     while q:
#         x = q.popleft()

#         D = (2 * x) % 10000
#         S = (x - 1) if x != 0 else 9999
#         L = (x % 1000) * 10 + (x // 1000)
#         R = (x % 10) * 1000 + (x // 10)

#         nx = [('D', D), ('S', S), ('L', L), ('R', R)]

#         for d, num in nx:
#             if not graph[num]:
#                 graph[num] = 1
#                 path[num] = path[x] + d
#                 if num == B:
#                     return path[num]
#                 q.append(num)

# for _ in range(T):
#     A, B = map(int, sys.stdin.readline().split())

#     graph = [0] * 10000
#     path = [''] * 10000
#     print(bfs(A, B))
