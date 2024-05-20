import sys

N = int(sys.stdin.readline())

scores = [0] * 301
for i in range(1, N+1):
    scores[i] = (int(sys.stdin.readline()))

result = [0] * 301
result[1] = scores[1]
result[2] = scores[1] + scores[2]
result[3] = max(scores[1] + scores[3], scores[2] + scores[3])

for i in range(4, N+1):
    result[i] = max((scores[i] + scores[i - 1] + result[i - 3]), (scores[i] + result[i - 2]))

print(result[N])
