import math



n = round(math.log(int(input()), 3))

S = [['*']]
for _ in range(n):
    t = ['' for _ in range(len(S) * 3)]

    for sy in range(len(S)):
        for sx in range(len(S[sy])):
            if S[sy][sx] == '*':
                ty = sy * 3
                t[ty] += "***"
                t[ty+1] += "* *"
                t[ty+2] += "***"
            else:
                ty = sy * 3
                t[ty] += "   "
                t[ty+1] += "   "
                t[ty+2] += "   "

    S = t

for s in S:
    print(s)
