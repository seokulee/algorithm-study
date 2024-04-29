import sys
from collections import deque

N = int(sys.stdin.readline())
d = deque()
result = list()

for idx, num in enumerate(map(int, sys.stdin.readline().split())):
    d.append((idx+1, num))

while len(d) > 1:
    idx, num = d.popleft()
    result.append(idx)

    if num > 0:
        for _ in range(num-1):
            d.append(d.popleft())
    else:
        for _ in range(-num):
            d.appendleft(d.pop())

idx, num = d.pop()
result.append(idx)

print(' '.join(map(str, result)))

# rotate 사용한...!

# N = int(sys.stdin.readline())
# paper = list(map(int, sys.stdin.readline().split()))
# result = list()

# d = deque()

# for i in range(N):
#     d.append((i+1, paper[i]))

# while d:
#     idx, p = d.popleft()
#     result.append(idx)
#     if not d:
#         break
#     d.rotate(-p if p < 0 else -p+1)

# print(' '.join(map(str, result)))  # 결과 출력
