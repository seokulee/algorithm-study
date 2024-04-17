_ = input()

cards = set(map(int, input().split()))

_ = input()
others_cards = list(map(int, input().split()))
for card in others_cards:
    if card in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
