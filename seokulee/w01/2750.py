# 수의 개수
N = int(input())

# N게의 줄에 정수가 주어진다.
arr = list()
for _ in range(N):
    arr.append(int(input()))

# 오름차순 정렬, 출력
arr.sort()
for i in arr:
    print(i)
