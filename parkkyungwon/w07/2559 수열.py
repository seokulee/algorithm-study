import sys



readline = sys.stdin.readline
N, K = map(int, readline().split())

arr = list(map(int, readline().split()))
arr.insert(0, 0)
for i in range(1, N+1):
    arr[i] += arr[i-1]

sums = tuple(arr[i+K] - arr[i] for i in range(N-K+1))
sys.stdout.write(str(max(sums)) + '\n')
