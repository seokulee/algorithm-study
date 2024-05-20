import sys

N = int(sys.stdin.readline())

if N == 1:
    print(1)
    sys.exit(0)

arr = list()
arr.append(1)
arr.append(2)

for _ in range(N-2):
    arr.append(sum(arr[-2:]) % 15746)

print(arr[-1])

# 메모리 사용량을 줄이기 위해서 계산한 모든 값을 저장하는 것이 아니라 15746으로 나눈 나머지를 저장한다.
# 1일때 예외처리

# Case 1 : memory 초과
# arr = list()
# arr.append(1)
# arr.append(2)
#
# for _ in range(N-2):
#     arr.append(sum(arr[-2:]))


# Case 2 : 시간 초과
# if N == 1:
#     print(1)
#     sys.exit()
#
# a = 1
# b = 2
# for _ in range(N-2):
#     a, b = b, a+b
