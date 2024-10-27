mapping = {char: num for char, num in zip(map(chr, range(97, 123)), range(1, 27))}
L = int(input())
total = 0

for char, i in zip(input().strip(), range(L)):
    total = (total + mapping[char] * 31**i) % 1234567891 

print(total)
