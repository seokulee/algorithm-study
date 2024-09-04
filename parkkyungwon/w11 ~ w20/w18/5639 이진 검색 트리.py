import sys
import bisect



sys.setrecursionlimit(10**7)

nodes = tuple(map(int, open(0).read().split()))
L = len(nodes)
answer = [None] * L

def sol(s, e, complement):
    if s == e: return

    v = nodes[s]
    answer[e-complement] = v
    complement += 1
    sep = bisect.bisect_left(nodes, v, lo=s+1, hi=e)
    sol(s+1, sep, complement), sol(sep, e, complement)

sol(0, L, 1)

print(*answer, sep='\n')
