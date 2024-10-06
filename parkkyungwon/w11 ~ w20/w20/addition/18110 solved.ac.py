import sys

N = int(input())
sep = (3*N + 10) // 20
arr = sorted(int(sys.stdin.readline()) for _ in range(N))

if sep: arr = arr[sep:-sep]
L = len(arr)

print((sum(arr)+ L//2)//L if L else 0)
