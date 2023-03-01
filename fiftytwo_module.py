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
    def build(self, deck_template, num):
        for i in range(num):
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
        
# This model does not support splits. we would need to implement multiple hands
class Player(): 
    def __init__(self, name):
        self.name = name
        self.cards = []
    def draw_card(self, deck):
        self.cards.append(deck.cards.pop())
    def show_hand(self):
        for i in range(len(self.cards)):
            self.cards[i].show()
    def show_upcard(self):
        print("{} has an upcard of".format(self.name))
        self.cards[0].show()
        # self.cards[0].show()
        
    def show(self):
        print("{} has a value of: {}".format(self.name, self.hand_value()))
        self.show_hand()
    def hand_value(self):
        sum = 0
        ace_count = 0
        for i in range(len(self.cards)):
            if self.cards[i].code == 'Ace':
                ace_count += 1
            sum += self.cards[i].value            
        # Subtract 10 for each ace until the count is below 21 or until were out of Aces to subtract
        for i in range(ace_count):
            if sum > 21:
                sum -= 10

        return sum

def play_blackjack():
    
    def evaluate_winner(player, dealer):
        if player.hand_value() > 21 and dealer.hand_value() > 21: # this should never happen, right? the dealer wouldn't hit if the player already busts
            return "Dealer"
        elif player.hand_value() > 21 and dealer.hand_value() <= 21:
            return "Dealer"
        elif player.hand_value() <= 21 and dealer.hand_value() > 21:
            return "Player"
        elif player.hand_value() < 21 and dealer.hand_value() < 21:
            if player.hand_value() > dealer.hand_value():
                return "Player"
            elif player.hand_value() < dealer.hand_value():
                return "Dealer"
            elif player.hand_value() == dealer.hand_value():
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