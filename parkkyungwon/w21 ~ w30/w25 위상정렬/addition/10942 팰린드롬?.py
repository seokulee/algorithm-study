import sys



def get_palindrome_dp(arr):
    dp = [[0] * N for _ in range(N)]

    # 자기 자신으로 만 이루어진 수
    for i in range(N): dp[i][i] = 1

    for i in range(N):
        # 홀수) 선택한 인덱스를 기준으로 포인터 두 개를 좌, 우 한칸씩 이동하며 검사
        for s, e in zip(range(i-1, -1, -1), range(i+1, N)):
            if arr[s] != arr[e]: break

            dp[s][e] = 1

        # 짝수)
        for s, e in zip(range(i, -1, -1), range(i+1, N)):
            if arr[s] != arr[e]: break

            dp[s][e] = 1

    return dp


readline = sys.stdin.readline
N = int(readline())
arr = tuple(map(int, readline().split()))

dp = get_palindrome_dp(arr)

M = int(readline())
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, readline().split())
    sys.stdout.write(str(dp[a][b]) + '\n')
