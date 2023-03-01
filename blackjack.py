import random

deck_template_standard = {
    'Ace'   : 11
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

deck_template_Aced = {
    'Ace'   : 11
    ,'Ace'   : 11
    ,'Ace'   : 11
    ,'Ace'   : 11
    ,'Ace'   : 11
    ,'Ace'   : 11
    ,'Ace'   : 11
    ,'Ace'   : 11
    ,'Ace'   : 11
    ,'Ace'   : 11
    ,'Ace'   : 11
    ,'Ace'   : 11
    ,'King'  : 10
}

class Card():
    def __init__(self, code, suit, value):
        self._code = code
        self._suit = suit
        self._value = value
    
    # def get_card(self):
    #     return [self._code, self._suit, self._value]
    def get_code(self):
        return self._code
    def get_suit(self):
        return self._suit
    def get_value(self):
        return self._value
    
    def show(self):
        print(f"{[self._code, self._suit, self._value]}")

class Deck():
    def __init__(self):
        self._cards = []
    def build(self, deck_template):
        for suit in ['Clubs', 'Hearts', 'Spades', 'Diamonds']:
            for dt in deck_template:
                card = Card(dt, suit, deck_template[dt])
                self._cards.append(card)
    def build(self, deck_template, num):
        for i in range(num):
            for suit in ['Clubs', 'Hearts', 'Spades', 'Diamonds']:
                for dt in deck_template:
                    card = Card(dt, suit, deck_template[dt])
                    self._cards.append(card)
    def show(self):
        for i in range(len(self._cards)):
            self._cards[i].show()
    def shuffle(self):
        for i in range(len(self._cards) - 1, 0, -1):
            r = random.randint(0, i)
            self._cards[i], self._cards[r] = self._cards[r], self._cards[i]
        
# This model does not support splits. we would need to implement multiple hands
class Player(): 
    def __init__(self, name):
        self._name = name
        self._cards = []

    def draw_card(self, deck):
        self._cards.append(deck._cards.pop())
    
    def show_hand(self):
        for i in range(len(self._cards)):
            self._cards[i].show()
    def show_upcard(self):
        print("{} has an upcard of".format(self._name))
        self._cards[0].show() 
    def show(self):
        print("{} has a value of: {}".format(self._name, self.get_hand_value()))
        self.show_hand()
    
    def get_card(self, i):
        if i >= (len(self._cards) - 1) or i < 0:
            return None
        else:
            return self._cards[i]
    def get_hand_value(self):
        sum = 0
        ace_count = 0
        for i in range(len(self._cards)):
            if self._cards[i]._code == 'Ace':
                ace_count += 1
            sum += self._cards[i].get_value()
        # Subtract 10 for each ace until the count is below 21 or until were out of Aces to subtract
        for i in range(ace_count):
            if sum > 21:
                sum -= 10
        return sum

def play_blackjack():
    
    def evaluate_winner(player, dealer):
        if player.get_hand_value() > 21 and dealer.get_hand_value() > 21: # this should never happen, right? the dealer wouldn't hit if the player already busts
            return "Dealer"
        elif player.get_hand_value() > 21 and dealer.get_hand_value() <= 21:
            return "Dealer"
        elif player.get_hand_value() <= 21 and dealer.get_hand_value() > 21:
            return "Player"
        elif player.get_hand_value() < 21 and dealer.get_hand_value() < 21:
            if player.get_hand_value() > dealer.get_hand_value():
                return "Player"
            elif player.get_hand_value() < dealer.get_hand_value():
                return "Dealer"
            elif player.get_hand_value() == dealer.get_hand_value():
                return "Push"
            else:
                return "Where are we (inner)?"
        else:
            return "Where are we (outer)?"
    
    # Create the deck
    deck = Deck()
    deck.build(deck_template_Aced,5)
    deck.shuffle()

    dealer = Player("Dealer")
    player = Player("Player1")
    
    dealer.draw_card(deck)
    player.draw_card(deck)
    dealer.draw_card(deck)
    player.draw_card(deck)

    if player.get_hand_value() == 21:
        if dealer.get_hand_value() == 21:
            return "Push"
        else:
            while dealer.get_hand_value() < 21:
                dealer.draw_card()
    # elif player.get_hand_value() < 21:
    #     if dealer.

    player.show()
    dealer.show_upcard()

    evaluate_winner(player, dealer)

play_blackjack()

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