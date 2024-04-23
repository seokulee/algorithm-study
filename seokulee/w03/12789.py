import sys

N = int(sys.stdin.readline())

line = [int(num) for num in sys.stdin.readline().split()]
line.reverse()
space = list()
turn = 1

while(True):
    if turn > N:
        print("Nice")
        break

    if line and line[-1] == turn:
        line.pop()
        turn += 1
    elif space and space[-1] == turn:
        space.pop()
        turn += 1
    elif line:
        space.append(line.pop())
    else:
        print("Sad")
        break

# 3달전 푼거 비교 조건을 다르게 했다.

# input = sys.stdin.readline
# n = int(input())
# wait = list(map(int, input().split()))
# tmp = []
# target = 1
# for i in wait:
# 	tmp.append(i)
# 	while tmp and tmp[-1] == target: # tmp 스택 하나로 비교
# 		tmp.pop()
# 		target += 1
# 	if len(tmp) > 1 and tmp[-1] > tmp[-2]:
# 		print("Sad")
# 		sys.exit()
# if tmp:
# 	print("Sad")
# else:
# 	print("Nice")

