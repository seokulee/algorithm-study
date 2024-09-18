import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

inorder_idx = {val: idx for idx, val in enumerate(inorder)}

def preorder(in_s, in_e, post_s, post_e):
    if in_s > in_e:
        return

    root = postorder[post_e]
    print(root, end=" ")

    root_idx = inorder_idx[root]
    offset = root_idx - in_s

    preorder(in_s, root_idx - 1, post_s, post_s + offset - 1)
    preorder(root_idx + 1, in_e, post_s + offset, post_e - 1)

preorder(0, N-1, 0, N-1)
