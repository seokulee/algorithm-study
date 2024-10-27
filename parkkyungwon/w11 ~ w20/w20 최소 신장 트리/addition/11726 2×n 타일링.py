def fib(n):
    if n == 1: return 1, 1, 0

    # 분할 정복
    a, b, c = fib(n//2)

    b_sq = b**2
    a, b, c = a**2 + b_sq, b*(a + c), b_sq + c**2

    # n이 홀수일 때
    if n % 2 == 1: 
        a, b, c = a+b, a, b

    # a, b, c는 피보나치 함수 f(n), f(n-1), f(n-2)이다
    return a % 10007, b % 10007, c % 10007

print(fib(int(input()))[0])
