list_of_cards = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    final_list_of_cards = []
    middle_of_deck = len(list_of_cards) // 2
    left_half = list_of_cards[:middle_of_deck]
    right_half = list_of_cards[middle_of_deck:]
    for card in range(middle_of_deck):
        final_list_of_cards.append(left_half[card])
        final_list_of_cards.append(right_half[card])
    list_of_cards = final_list_of_cards
print(list_of_cards)

