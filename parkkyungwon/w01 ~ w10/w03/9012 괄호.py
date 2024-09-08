import sys



readline = sys.stdin.readline
writeline = sys.stdout.writelines

n = int(readline())

for _ in range(n):
    ps = readline().strip()

    c = 0
    for s in ps:
        if '(' == s:
            c += 1

        else:
            c -= 1

            if c < 0:
                writeline('NO\n')
                break

    else:
        if c > 0:
            writeline('NO\n')

        else:
            writeline('YES\n')
