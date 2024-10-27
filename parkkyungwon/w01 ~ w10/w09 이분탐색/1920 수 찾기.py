import sys



readline = sys.stdin.readline
write = sys.stdout.write
readline()
s = set(readline().split())
readline()

for i in tuple(readline().split()):
    if i in s:
        write('1\n')
    else:
        write('0\n')
