import sys

N, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 내림차순 정렬
arr.sort(reverse=True)

# 커트라인 = k번째 높은 점수(index -> k-1)
print(arr[k - 1])

