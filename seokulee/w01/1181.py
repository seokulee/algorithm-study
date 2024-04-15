import sys

input = sys.stdin.readline

N = int(input())

arr = set()

for _ in range(N):
    arr.add(input().rstrip())

sorted_arr = sorted(arr, key=lambda s : (len(s), s))

print(*sorted_arr, sep='\n', end='')
