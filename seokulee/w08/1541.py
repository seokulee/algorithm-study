import sys

line = list(sys.stdin.readline().rstrip().split('-'))

result = sum(list(map(int, line[0].split('+'))))
for part in line[1:]:
    result -= sum(list(map(int, part.split('+'))))

print(result)

# eval 쓰는 방법인데 0009를 int로 인식 못함.

# result = 0
# while line.find('-') != -1:
#     if result == 0:
#         result += eval(line[:line.find('-')])
#     else:
#         result -= eval(line[:line.find('-')])
#     line = line[line.find('-')+1:]
#
#     # print(result, line)
#
# if line and result == 0:
#     result += eval(line)
# elif line and result != 0:
#     result -= eval(line)
#
# print(result)