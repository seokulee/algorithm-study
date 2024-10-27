import sys
    


readline = sys.stdin.readline


len_N = int(readline())
N = list(map(int, readline().split()))

c_max = g_max = N[0]
for n in N[1:]:
    c_max = max(n, c_max + n)
    g_max = max(g_max, c_max)

sys.stdout.write(str(g_max) + '\n')
