import math
from functools import lru_cache



N, K = map(int, input().split())
arr = list(map(int, input().split()))

# n 크기의 배열을 정렬할 때 총 저장되는 횟수를 반환
@lru_cache()
def check(n):
    if not n: return 0
    
    a = int(math.log2(n))
    b = 2 ** a

    return a*b + (a + 2)*(n - b)

def sol(n, k):
    def f(s, e, k):
        m = (s+e+1) // 2
        # 전반부 정렬에 저장되는 횟수
        left = check(m-s)

        if left >= k: return f(s, m, k)
        k -= left

        # 후반부 정렬에 저장되는 횟수
        right = check(e-m)

        if right >= k: return f(m, e, k)
        k -= right    

        # 위 정렬에 저장된게 아니면, 병합 때 발생
        return sorted(arr[s:e])[k-1]

    return -1 if check(n) < k else f(0, n, k)

print(sol(N, K))
