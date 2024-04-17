from collections import defaultdict


cards = defaultdict(lambda: 0)
count = int(input())
for i in map(int, input().split()):
    cards[i] += 1

count = int(input())
for i in map(int, input().split()):
    print(cards[i], end=' ')
