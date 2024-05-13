import sys

def hanoi(N, s, e, o):
    if N == 1:
        print(s, e)
        return

    hanoi(N-1, s, o, e)
    print(s, e)
    hanoi(N-1, o, e, s)

N = int(sys.stdin.readline())

print(2**N - 1)
hanoi(N, 1, 3, 2)
