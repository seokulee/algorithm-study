import sys



write = sys.stdout.write

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break

    arr = [i for i in range(1, n) if n % i == 0]

    t = sum(arr)
    if n == t:
        write(str(t) + ' = ' + ' + '.join(map(str, arr)) + '\n')

    else:
        write(str(n) + ' is NOT perfect.\n')
