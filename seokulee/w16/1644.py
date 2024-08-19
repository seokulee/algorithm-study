import sys

N = int(sys.stdin.readline().rstrip())

def eratosthenes(num:int = 1000000):
    MAX = num + 1
    LIM = int(num ** 0.5) + 1
    RSET = lambda start, end, gap: set(range(start, end, gap))

    prime = RSET(5, MAX, 6) | RSET(7, MAX, 6)
    if num > 2: prime.add(3)
    if num > 1: prime.add(2)
    for i in range(5, LIM, 6):
        if i in prime:
            prime -= RSET(i * i, MAX, i * 6) | RSET(i * (i + 2), MAX, i * 6)
        j = i + 2
        if j in prime:
            prime -= RSET(j * j, MAX, j * 6) | RSET(j * (j + 4), MAX, j * 6)

    return sorted(prime)

arr = list(eratosthenes(N))

s = e = 0
len_arr = len(arr)
sum_value = 0
count = 0

while s < len_arr:
    if sum_value == N:
        count += 1
        sum_value -= arr[s]
        s += 1
    elif sum_value < N and e < len_arr:
        sum_value += arr[e]
        e += 1
    else:
        sum_value -= arr[s]
        s += 1


print(count)
