from collections import defaultdict


cards = defaultdict(lambda: 0)

_ = input()
for i in map(int, input().split()):
    cards[i] += 1

_ = input()
for i in map(int, input().split()):
    print(cards[i], end=' ')
