import sys

N = int(sys.stdin.readline())
f = [0 for i in range(N+1)]
f[1] = f[2] = 1
# c_1 = c_2 = 0


# def fib(N):
#     if N == 1 or N == 2:
#         global c_1
#         c_1 += 1
#         return 1
#     else:
#         return fib(N - 1) + fib(N - 2)
def fib(N):
    a, b = 1, 1
    for _ in range(3, N+1):
        a, b = b, a + b

    return b


# def fibonacci(N):
#     for i in range(3, N+1):
#         global c_2
#         c_2 += 1
#         f[i] = f[i - 1] + f[i - 2]
#     return f[N]
def fibonacci(N):
    return N - 2


print(fib(N), fibonacci(N))
