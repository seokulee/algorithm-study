import sys
sys.setrecursionlimit(10**6)

preorder = []
while True:
    try:
        num = int(sys.stdin.readline())
        preorder.append(num)
    except:
        break

def postorder(s, e):
    if s > e:
        return

    root = preorder[s]
    m = e + 1
    for i in range(s + 1, e + 1):
        if preorder[i] > root:
            m = i
            break

    postorder(s + 1, m - 1)
    postorder(m, e)
    print(root)


postorder(0, len(preorder) - 1)
