import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 중복 제거, 정렬
sorted_arr = sorted(set(arr))

# 딕셔너리를 사용하여 각 원소의 인덱스 저장
index_map = {value: idx for idx, value in enumerate(sorted_arr)}

# 결과 계산
result = ' '.join(str(index_map[x]) for x in arr)

print(result)
