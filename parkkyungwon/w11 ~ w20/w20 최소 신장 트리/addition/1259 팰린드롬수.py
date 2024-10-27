import sys

while 1:
    string = sys.stdin.readline().rstrip()

    if string == '0': break

    sys.stdout.write('yes\n' if string == string[::-1] else 'no\n')
