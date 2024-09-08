import sys



def power(arr, ex, M):
    arr = [[a % M for a in ar] for ar in arr]
    arr_T = [ar for ar in zip(*arr)]
    
    def p(ex):
        if ex == 1:
            return arr
        
        # 지수의 절반
        A = p(ex//2)
        # 행렬 곱을 쉽게 하기위해 A의 전치 행렬을 구함
        B = [a for a in zip(*A)]
        # A행렬 제곱
        C = [[sum(x*y for x, y in zip(a, b)) % M for b in B] for a in A]

        # 지수가 홀수면 C에 전치행렬 arr_T를 추가로 곱해줌
        return C if ex % 2 == 0 else [[sum(x*y % M for x, y in zip(a, b)) % M for b in arr_T] for a in C]

    return p(ex)


readline = sys.stdin.readline
N, B = map(int, readline().split())
arr = [tuple(map(int, readline().split())) for _ in range(N)]

for ar in power(arr, B, 1000):
    sys.stdout.write(' '.join(map(str, ar)) + '\n')
