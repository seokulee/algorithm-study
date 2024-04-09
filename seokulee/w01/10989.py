# 수의 범위가 작다면 카운팅 정렬을 사용하여 더욱 빠르게 정렬할 수 있습니다.
import sys
input = sys.stdin.readline
print = sys.stdout.write

#계수정렬 활용
n = int(input())
arr = [0] * (10000 + 1) # 입력값이 10000개까지 주어지니 10000 + 1개의 리스트 선언

#각 입력값에 해당하는 인덱스의 값 증가
for _ in range(n):
    arr[int(input())] += 1

#arr에 기록된 정보 확인
for i in range(len(arr)):
    if arr[i] != 0: #0이 아닌 데이터, 즉 입력받은 데이터들을 출력
        for _ in range(arr[i]):
            print(str(i) + '\n')
