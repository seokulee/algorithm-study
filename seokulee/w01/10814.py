import sys

input = sys.stdin.readline

N = int(input())

arr = list()
for i in range(N):
    age, name = input().split()
    age = int(age)
    arr.append((i, age, name))

arr.sort(key=lambda info : (info[1], info[0]))

for i, age, name in arr:
    print(age, name)
