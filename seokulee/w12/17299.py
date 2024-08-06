import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
counter = Counter(A)
stack = list()
answer = [-1 for _ in range(N)]
for i in range(N):
    while stack and counter[A[stack[-1]]] < counter[A[i]]:
        answer[stack.pop()] = A[i]
    stack.append(i)


print(*answer)
