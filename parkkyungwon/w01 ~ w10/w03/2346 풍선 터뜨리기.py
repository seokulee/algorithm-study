from collections import deque



def readjust(j, balloon: deque):
    l = len(balloon)
    if j > 0:
        j -=1
        
    j %= l
    if j > l // 2:
        j -= l

    elif j < -l // 2:
        j += l

    if j > 0:
        for _ in range(j):
            balloon.append(balloon.popleft())
    
    else:
        for _ in range(-j):
            balloon.appendleft(balloon.pop())
    
N = int(input())

jump = list(map(int, input().split()))
balloon = deque()
for k, v in zip(range(1, N+1), jump):
    balloon.append((k, v))

for _ in range(N-1):
    num, j = balloon.popleft()
    print(num, end=' ')

    readjust(j, balloon)

num, j = balloon.popleft()
print(num)
