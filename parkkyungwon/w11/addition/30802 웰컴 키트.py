N = int(input())
t_shirts = (*map(int, input().split()), )
T, P = map(int, input().split())

t = sum(((v-1) // T) + 1 for v in t_shirts)

print(t)
print(N // P, N % P)
