arr = list()

# 5개의 자연수가 주어짐
for _ in range(5):
    arr.append(int(input()))

# 정렬
arr.sort()

# 평균
print(sum(arr)//5)
# 중앙값
print(arr[2])
