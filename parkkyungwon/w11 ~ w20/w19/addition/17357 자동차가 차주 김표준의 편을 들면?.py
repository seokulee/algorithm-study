import sys


def sol(arr):
    sums = [0] + arr
    sqsums = [0] * (N+1)

    for i in range(N):
        sums[i+1] += sums[i]
        sqsums[i+1] = sqsums[i] + arr[i]**2
    
    for k in range(1, N+1):
        maxi_vari = -1
        maxi_idx = 0

        for s, e in zip(range(N+1-k), range(k, N+1)):
            # mean을 k를 나누고 vari의 첫 항을 k로 나눠야 하지만, 나누어서 소수를 사용하면 연산에 시간이 많이 소요됨
            # 문제는 정확한 표준 편차 값이 필요한게 아닌 대소 구분만 해주면 되기 때문에, k**2을 곱해도 문제가 요구하는 답에 충족함
            mean = (sums[e] - sums[s]) 
            vari = (sqsums[e] - sqsums[s])*k - mean**2

            if vari > maxi_vari:
                maxi_vari = vari
                maxi_idx = s+1
    
        yield maxi_idx


N = int(input())
arr = list(map(int, input().split()))

for s in sol(arr):    
    sys.stdout.write(str(s) + '\n')
