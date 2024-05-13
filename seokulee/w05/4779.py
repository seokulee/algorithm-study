import sys

def cantor(N:int, line:str):
    if N == 0:
        return line

    p1 = len(line) // 3
    p2 = (len(line) // 3) * 2

    s1 = cantor(N-1, line[:p1])
    s2 = ' ' * (p2 - p1)
    s3 = cantor(N-1, line[p2:])

    line = s1 + s2 + s3

    return line


while True:
    N = sys.stdin.readline()
    if N == '':
        sys.exit()
    N = int(N)
    line = '-' * (3 ** N)

    print(cantor(N, line))
