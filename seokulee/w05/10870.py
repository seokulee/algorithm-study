import sys

N = int(sys.stdin.readline())

def Fibonacci(N: int):
    if N == 1:
        return 1
    elif N == 0:
        return 0

    return Fibonacci(N-1) + Fibonacci(N-2)

print(Fibonacci(N))
