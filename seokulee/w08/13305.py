import sys

N = int(sys.stdin.readline())
D = list(map(int, sys.stdin.readline().split()))
P = list(map(int, sys.stdin.readline().split()))

old_price = P[0]
total_price = 0
moved_distance = 0
for distance, price in zip(D, P[1:]):
    moved_distance += distance
    if price < old_price:
        total_price += moved_distance * old_price
        moved_distance = 0
        old_price = price

if moved_distance > 0:
    total_price += moved_distance * old_price

print(total_price)
