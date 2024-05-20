import sys

N = int(sys.stdin.readline())

wine = [0] * 10001
for i in range(1, N+1):
    wine[i] = (int(sys.stdin.readline()))

result = [0] * 10001
result[1] = wine[1]
result[2] = wine[1] + wine[2]
result[3] = max(wine[1] + wine[3], wine[2] + wine[3], wine[1] + wine[2])

for i in range(4, N+1):
    result[i] = max((wine[i] + wine[i - 1] + result[i - 3]), (wine[i] + result[i - 2]), result[i - 1])

print(result[N])