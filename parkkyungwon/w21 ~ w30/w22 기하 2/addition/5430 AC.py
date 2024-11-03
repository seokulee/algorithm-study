import sys



def sol(command, arr):
    command = tuple(map(len, command.rstrip().split(sep='R')))
    arr = arr[1:-2].split(sep=',')

    if arr == ['']:
        arr = []
    
    s = sum(command[::2]) 
    e = len(arr) - sum(command[1::2]) 

    if s > e:
        return 'error\n'

    else:
        arr = arr[s:e]
        if len(command) % 2 == 0: arr.reverse()

        return '[' + ','.join(arr) + ']\n'


readline = sys.stdin.readline
T = int(readline())

for _ in range(T):
    command = readline()
    readline()
    arr = readline()
    
    sys.stdout.write(sol(command, arr))
