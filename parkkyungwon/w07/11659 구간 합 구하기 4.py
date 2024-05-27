import sys



readline = sys.stdin.readline
N, M = map(int, readline().split())

arr = [0] + list(map(int, readline().split()))
for i in range(1, N+1):
    arr[i] += arr[i-1]

for _ in range(M):
    i, j = map(int, readline().split())
    
    sys.stdout.write(str(arr[j] - arr[i-1]) + '\n')
