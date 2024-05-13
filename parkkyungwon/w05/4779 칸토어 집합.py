import sys


while True:
    n = sys.stdin.readline()
    if n == '':
        break

    n = int(n)
    s = '-'
    for _ in range(n):
        s = s + ' ' * len(s) + s

    sys.stdout.write(s + '\n')
