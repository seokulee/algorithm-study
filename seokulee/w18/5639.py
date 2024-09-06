import sys
sys.setrecursionlimit(10**6)

preorder = []
while True:
    try:
        num = int(sys.stdin.readline())
        preorder.append(num)
    except:
        break

def postorder(arr):
    if not arr:
        return

    left, right = [], []
    mid = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > mid:
            left = arr[1:i]
            right = arr[i:]
            break
        else:
            left = arr[1:]

    postorder(left)
    postorder(right)
    print(mid)


postorder(preorder)
