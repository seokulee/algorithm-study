import sys



count = int(input())

for _ in range(count):
    n = int(sys.stdin.readline())

    quarter = n // 25
    n %= 25

    dime = n // 10
    n %= 10

    nickel = n // 5 

    penny = n % 5

    s = map(str, (quarter, dime, nickel, penny))
    sys.stdout.write(' '.join(s) + '\n')
