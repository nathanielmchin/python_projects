import bj_rules as b
import cards
import player

# Initalize deck and players (only works for one player right now)
def init_game(num_decks=1):
    d = cards.Deck(num_decks)
    p = player.Player('Anthony')

    dealer = player.Player('Dealer')
    d.shuffle()
    return d, p, dealer

def hit(person, d):
    person.add_card(d._cards.pop())

def deal(d, p, dealer):
    p.add_card(d._cards.pop())
    dealer.add_card(d._cards.pop())
    p.add_card(d._cards.pop())
    dealer.add_card(d._cards.pop())

    p._val = b.get_values(p._suitless_hand)
    dealer._val = b.get_values(dealer._suitless_hand)

def show(p, dealer):
    p.show_hand()
    dealer.show_top()

def displayOptions():
    return """
##############################################
# 1 - HIT | 2 - STAND | 3 - SPLIT | 4 DOUBLE #
##############################################
"""

def options(choice, p, d):
    if choice == 1:
        hit(p, d)
    elif choice == 2:
        p._val = b.highest_val(p._val)
    elif choice == 3:
        return True
    else:
        return True


if __name__ == "__main__":
    deck, players, dm = init_game()

    deal(deck, players, dm)
    show(players, dm)
    res = input(displayOptions())
    options(res,players,deck)
    show(players, dm)

###### CODE BELOW FOR TESTING - PLACE IN MAIN ###########

    # deck, players, dealer = init_game()

    # ##### Test Run - VALIDATING DECKS + Player

    # # Size should be 52 | 54 with Joker
    # print(len(deck._cards))

    # # Print every card
    # for card in deck._cards:
    #     print(card.get_code())

    # deck.shuffle()
    # print("--------------------")
    # # Print every card
    # for card in deck._cards:
    #     print(card.get_code())


    # players.add_card(deck._cards.pop())
    # dealer.add_card(deck._cards.pop())
    # players.add_card(deck._cards.pop())
    # dealer.add_card(deck._cards.pop())

    # players.show_hand()
    # dealer.show_top()
    # players._val = b.get_values(players._suitless_hand)
    # dealer._val = b.get_values(dealer._suitless_hand)
    # ##### Test Run - VALIDATING DECKS
