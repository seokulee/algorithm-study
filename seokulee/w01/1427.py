import sys

input = sys.stdin.readline
print = sys.stdout.write

# str -> list
num_arr = list(input())
# 각 자리의 문자 type의 숫자를 내림차순
num_arr.sort(reverse=True)

# print = sys.stdout.write 이므로 개행없음
# or print(i, end='')
for i in num_arr:
    print(i)

# 예전에 한 거
# import sys

# N = sys.stdin.readline().rstrip()

# arr = list(N)
# print(*sorted(arr,reverse=True), sep='')
