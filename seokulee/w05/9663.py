import sys

N = int(sys.stdin.readline())

def dfs(r, count, h_checker, d_checker, ad_checker):
    if r == N:
        count[0] += 1
        return

    for j in range(N):
        if not (h_checker[j] or d_checker[r+j] or ad_checker[r-j+N]):
            h_checker[j] = d_checker[r+j] = ad_checker[r-j+N] = True
            dfs(r+1, count, h_checker, d_checker, ad_checker)
            h_checker[j] = d_checker[r+j] = ad_checker[r-j+N] = False

def n_queens(N):
    count = [0]
    h_checker = [False for _ in range(N)]
    d_checker = [False for _ in range(N*2)]
    ad_checker = [False for _ in range(N*2)]
    dfs(0, count, h_checker, d_checker, ad_checker)

    return count[0]

print(n_queens(N))
