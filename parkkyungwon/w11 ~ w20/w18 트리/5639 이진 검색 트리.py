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
    # 루트를 사용해서 왼쪽은 모든 값이 루트보다 작고, 오른쪽은 모든 값이 크기 때문에 이진탐색이 가능
    # 이진 탐색이 완료되면 좌, 우 서브트리 내에서 다시 루트를 사용해서 이진탐색
    sep = bisect.bisect_left(nodes, v, lo=s+1, hi=e)
    sol(s+1, sep, complement), sol(sep, e, complement)

sol(0, L, 1)

print(*answer, sep='\n')
