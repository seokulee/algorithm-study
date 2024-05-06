import sys


writeline = sys.stdout.write
readline = sys.stdin.readline

count = int(input())

for _ in range(count):
    S = readline().strip()
    call_count = 0

    for i in range(len(S)//2):
        call_count += 1
        if S[i] != S[-(i+1)]:
            writeline('0 ')
            break

    else:        
        call_count += 1
        writeline('1 ')

    writeline(f'{call_count}\n')
