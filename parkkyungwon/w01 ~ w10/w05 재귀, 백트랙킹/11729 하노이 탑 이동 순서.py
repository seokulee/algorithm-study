import sys



writeline = sys.stdout.write


def top(count):
    s, m, d = [i for i in range(n, -1, -1)], [], []

    if n % 2 == 0:
        first = (s, m, '1', '2')
        second = (s, d, '1', '3')
    else:
        first = (s, d, '1', '3')
        second = (s, m, '1', '2')
    third = (m, d, '2', '3')

    while True:
        for target in first, second, third:
            if not len(target[0]):
                target[0].append(target[1].pop())
                yield target[3], target[2]

            elif not len(target[1]):
                target[1].append(target[0].pop())
                yield target[2], target[3]

            elif target[0][-1] > target[1][-1]:
                target[0].append(target[1].pop())
                yield target[3], target[2]

            else:
                target[1].append(target[0].pop())
                yield target[2], target[3]

            count -= 1
            if not count:
                return
        

n = int(input())

count = 2**n - 1

writeline(str(count) + '\n')
      
for a, b in top(count):
    writeline(a + ' ' + b + '\n')
