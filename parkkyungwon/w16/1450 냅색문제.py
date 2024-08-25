import bisect
from collections import defaultdict



def cases(arr, maxi):
    dp = defaultdict(int)
    dp[0] = 1

    for weight in arr:
        new_dp = dp.copy()
        for current_sum in dp:
            new_sum = current_sum + weight
            if new_sum <= maxi:
                new_dp[new_sum] += dp[current_sum]
        dp = new_dp

    return dp


def sumat(a, b, maxi):
    # 오른쪽 배열은 정렬과 누적합을 미리 구한다
    b_keys = sorted(b.keys())
    b_sums = [b[b_keys[i]] for i in range(len(b_keys))]
    for i in range(len(b_sums)-1):
        b_sums[i+1] += b_sums[i]

    # 구하려는 값 max값을 넘지않는 값만 더해준다
    count = 0
    for ak in a:
        bk = bisect.bisect_right(b_keys, maxi - ak) - 1
        count += a[ak] * b_sums[bk]

    return count


L, C = map(int, input().split())
arr = tuple(map(int, input().split()))

m = L // 2
left = cases(arr[:m], C)
right = cases(arr[m:], C)

print(sumat(left, right, C))
