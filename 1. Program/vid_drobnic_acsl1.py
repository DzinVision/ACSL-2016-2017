# Vid Drobnič
# Gimnazija Vič, 4.b
# Intermediate 3
# Language: Python 3.5.2

def card_rank(card):
    try:
        return int(card[0])
    except:
        string_rank = card[0]
        if string_rank == 'A':
            return 1
        if string_rank == 'K':
            return 13
        if string_rank == 'Q':
            return 12
        if string_rank == 'J':
            return 11
        if string_rank == 'T':
            return 10


for _ in range(5):
    lead_card, *cards = input().split()
    suit = lead_card[1]
    rank = card_rank(lead_card)

    cards_with_higher_rank = []
    same_suit_cards = []

    for card in cards:
        if card[1] == suit:
            if card_rank(card) > rank:
                cards_with_higher_rank.append(card)
            same_suit_cards.append(card)

    if len(cards_with_higher_rank) > 0:
        print(sorted(cards_with_higher_rank, key=card_rank)[0])
    elif len(same_suit_cards) > 0:
        print(sorted(same_suit_cards, key=card_rank)[0])
    else:
        print(sorted(cards, key=card_rank)[0])
