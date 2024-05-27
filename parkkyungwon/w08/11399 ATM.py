N = int(input())
arr = list(map(int, input().split()))
arr.sort()

t = 0
for i in range(N):
    t += arr[i] * (N-i)

print(t)
