import sys

def recursion(line, start, end, count):
    count += 1
    if start >= end:
        return 1, count
    elif line[start] != line[end]:
        return 0, count
    else:
        return recursion(line, start + 1, end - 1, count)

def isPalindrome(line, count):
    return recursion(line, 0, len(line) -1, count)

T = int(sys.stdin.readline())

for _ in range(T):
    count = 0
    line = sys.stdin.readline().rstrip()
    result, count = isPalindrome(line, count)
    print(result, count)
