# 소수 체
def sieve(arr):
    L = len(arr)

    for i in range(int(L**(0.5)) + 1):
        if arr[i]:
            for j in range(i**2, L, i):
                arr[j] = False


# 누적 합과 투 포인터를 사용
def sol(arr, x):
    L = len(arr)
    s, e, count = 0, 1, 0

    while e < L:
        a = arr[e] - arr[s]
        if a == x:
            count += 1
            s += 1
            e += 1
        elif a < x:
            e += 1
        else:
            s += 1

    return count


N = int(input())
arr = [True] * (N+1)
arr[0], arr[1] = False, False
sieve(arr)

# 소수만 찾아서 누적합 계산
prev = 0
sums = [0] + [prev := (prev + i) for i in range(1, N+1) if arr[i]]

print(sol(sums, N))