import sys



write = sys.stdout.write

def print_star(n, i):
    write(''.join([' '] * (n - i)))
    write(''.join(['*'] * (i * 2 - 1)) + '\n')


n = int(input())

for i in range(1, n + 1):
    print_star(n, i)
    
for i in range(n - 1, 0, -1):
    print_star(n, i)
