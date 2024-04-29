from collections import deque



n, k = map(int, input().split())
n_dq = deque(range(1, n + 1))

print('<', end='')
for _ in range(len(n_dq) - 1):
    for _ in range(k-1):
        n_dq.append(n_dq.popleft())
    print(n_dq.popleft(), end=', ')

print(n_dq.pop(), '>', sep='')
