import sys

input = sys.stdin.readline

N = input()
owned = set(map(int, input().split())) # -10_000_000 ~ 10_000_000 중복 x


M = input()
checked = list(map(int, input().split()))

print(' '.join(['1' if i in owned else '0' for i in checked]))
