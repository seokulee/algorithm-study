import sys



n = int(sys.stdin.readline())

a, b = 1, 2
for _ in range(n-1):
    a, b = b, (a + b) % 15746

sys.stdout.write(str(a) + '\n')
