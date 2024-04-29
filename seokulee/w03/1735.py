import sys
import math

X_1, X_2 = map(int, sys.stdin.readline().split())
Y_1, Y_2 = map(int, sys.stdin.readline().split())

Z_1 = X_2 * Y_1 + Y_2 * X_1
Z_2 = X_2 * Y_2

while True:
    gcd = math.gcd(Z_1, Z_2)
    if gcd == 1:
        break
    Z_1 = Z_1//gcd
    Z_2 = Z_2//gcd

print(Z_1, Z_2)
