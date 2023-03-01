import random

deck_template_standard = {
    'Ace'   : 1
    ,'2'     : 2
    ,'3'     : 3
    ,'4'     : 4
    ,'5'     : 5
    ,'6'     : 6
    ,'7'     : 7
    ,'8'     : 8
    ,'9'     : 9
    ,'10'    : 10
    ,'Jack'  : 10
    ,'Queen' : 10
    ,'King'  : 10
}

class Card():
    def __init__(self, code, suit, value):
        self.code = code
        self.suit = suit
        self.value = value
    def card(self):
        return [self.code, self.suit, self.value]
    def show(self):
        print (self.card())

class Deck():
    def __init__(self):
        self.cards = []
    def build(self, deck_template):
        for suit in ['Clubs', 'Hearts', 'Spades', 'Diamonds']:
            for dt in deck_template:
                card = Card(dt, suit, deck_template[dt])
                self.cards.append(card)
    def show(self):
        for i in range(len(self.cards)):
            self.cards[i].show()
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []
    def draw_card(self, deck):
        self.cards.append(deck.cards.pop())
    def show_hand(self):
        for i in range(len(self.cards)):
            self.cards[i].show()
    def show(self):
        print("{} has a value of: {}".format(self.name, self.hand_value()))
        self.show_hand()
    def hand_value(self):
        sum = 0
        for i in range(len(self.cards)):
            # how do I handle aces for 1/11?
            # if self.cards[i].value == 1:
                # sum += 10
            sum += self.cards[i].value
        return sum

# deck = Deck()
# deck.build(deck_template_standard)
# deck.shuffle()
# # deck.show()

# p1 = Player("Nathan")
# p1.draw_card(deck)
# p1.draw_card(deck)
# p1.show_hand()
# p1.show()

# # deck.show()