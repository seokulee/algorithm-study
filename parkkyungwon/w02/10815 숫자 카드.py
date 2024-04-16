count = int(input())

cards = set()
cards.update(list(map(int, input().split())))

count = int(input())
others_cards = list(map(int, input().split()))
for card in others_cards:
    if card in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
