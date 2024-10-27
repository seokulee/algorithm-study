import re



def get_sum(t):
    return sum(map(int, re.split('\+|\-', t)))


arr = input().split('-', 1)

c = get_sum(arr[0])
if len(arr) != 1:
    c -= get_sum(arr[1])

print(c)
