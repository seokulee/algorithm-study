import sys



def traversal(i): 
    if order == 0: yield i
    if edge[i][0]: yield from traversal(edge[i][0])
    if order == 1: yield i
    if edge[i][1]: yield from traversal(edge[i][1])
    if order == 2: yield i


readline = sys.stdin.readline
N = int(readline())
edge = {}

for root, left, right in (readline().split() for _ in range(N)):
    edge[root] = (None if left == '.' else left, None if right == '.' else right)

for order in range(3): 
    print(''.join(traversal('A')))
