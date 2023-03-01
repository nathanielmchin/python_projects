import cards

d = cards.Deck()

# Test Run
# Size should be 52 | 54 with Joker
print(len(d._cards))

# Print every card
for card in d._cards:
    print(card.get_code())

