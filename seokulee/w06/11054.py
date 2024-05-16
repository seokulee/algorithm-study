import sys


def solution():
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    inc_cnt = [1 for _ in range(N)]
    dec_cnt = [1 for _ in range(N)]

    for i in range(1, N):
        inc_v = 0
        dec_v = 0
        for j in range(i, -1, -1):
            if arr[i] > arr[j] > inc_v:
                inc_v = arr[j]
                inc_cnt[i] = max(inc_cnt[i], inc_cnt[j] + 1)
            if arr[-i-1] > arr[-j-1] > dec_v:
                dec_v = arr[-j-1]
                dec_cnt[-i-1] = max(dec_cnt[-i-1], dec_cnt[-j-1] + 1)

    result = [inc + dec - 1 for inc, dec in zip(inc_cnt, dec_cnt)]

    return max(result)


if __name__ == '__main__':
    print(solution())
