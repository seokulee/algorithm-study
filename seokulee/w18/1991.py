import sys

LEFT, RIGHT = 0, 1
N = int(sys.stdin.readline())
tree = {}

for _ in range(N):
    parent, left, right = sys.stdin.readline().split()
    tree[parent] = [left, right]


def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][LEFT])
        preorder(tree[root][RIGHT])


def inorder(root):
    if root != '.':
        inorder(tree[root][LEFT])
        print(root, end='')
        inorder(tree[root][RIGHT])


def postorder(root):
    if root != '.':
        postorder(tree[root][LEFT])
        postorder(tree[root][RIGHT])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')

