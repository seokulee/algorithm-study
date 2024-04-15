import sys

input = sys.stdin.readline

N = int(input())

arr = list()

for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

# 좌표 정렬
arr.sort(key=lambda point: (point[1], point[0]))

# 정렬된 좌표 출력
for point in arr:
    print(point[0], point[1])
