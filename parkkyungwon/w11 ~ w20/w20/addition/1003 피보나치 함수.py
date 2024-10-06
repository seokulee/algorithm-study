def fib(n):
    def f(n):
        if n == 1: return 1, 1, 0

        # 분할 정복
        a, b, c = f(n//2)

        b_sq = b**2
        a, b, c = a**2 + b_sq, b*(a + c), b_sq + c**2

        # n이 홀수일 때
        if n % 2 == 1: 
            a, b, c = a+b, a, b

        # a, b, c는 피보나치 함수 f(n), f(n-1), f(n-2)이다
        return a, b, c
    
    match n:
        case 0: return '1 0'
        case 1: return '0 1'
        case _: 
            ret = f(n - 1)
            return f'{ret[1]} {ret[0]}'


ss = open(0).read().splitlines()
print(*(fib(int(s)) for s in ss[1:]), sep='\n')
