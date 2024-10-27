import math



for _ in range(int(input())):
    K, N = map(int, input().split())

    print(math.comb(N, K))
