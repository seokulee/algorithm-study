import sys

# 수의 개수
N = int(sys.stdin.readline())

# N게의 줄에 정수가 주어진다.
arr = list()
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

# 오름차순 정렬, 출력
arr.sort()
for i in arr:
    print(i)
