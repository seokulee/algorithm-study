import sys



readline = sys.stdin.readline
write = sys.stdout.write

while True:
    a, b = map(int, readline().split())
    if a == 0 and b == 0:
        break
    
    if a % b == 0:
        write('multiple')

    elif b % a == 0:
        write('factor')

    else:
        write('neither')

    write('\n')
