import random
import time

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

deck_template_17 = {
    't'   : 10
    ,'17'   : 7
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

    def build(self, deck_template, num = 1):
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
    def show_card(self, i = 0):
        if i >= (len(self._cards) - 1) or i < 0:
            return None
        else:
            print("{} has an upcard of".format(self._name))
            self._cards[i].show() 
    def show(self):
        print("{} has a value of: {}".format(self._name, self.get_hand_value()))
        self.show_hand()
    
    def get_card(self, i):
        if i >= (len(self._cards) - 1) or i < 0:
            return None
        else:
            return self._cards[i]
    def find_card(self, name):
        for i in range(len(self._cards)):
            if name == self._cards[i].get_code():
                return True
        return False
    def get_hand_value(self):
        sum = 0
        ace_count = 0
        for i in range(len(self._cards)):
            if self._cards[i]._code == 'Ace':
                ace_count += 1
            # print(f"looking at card:") 
            # self._cards[i].show()
            sum += self._cards[i].get_value()
        # Subtract 10 for each ace until the count is below 21 or until were out of Aces to subtract
        for i in range(ace_count):
            if sum > 21:
                sum -= 10
        return sum

def play_blackjack():
    
    # Method for evaluating the winner of a round of blackjack
    def evaluate_winner(player, dealer):
        if player.get_hand_value() > 21 and dealer.get_hand_value() > 21: # this should never happen, right? the dealer wouldn't hit if the player already busts
            return "Dealer"
        elif player.get_hand_value() > 21 and dealer.get_hand_value() <= 21: # player busts
            return "Dealer"
        elif player.get_hand_value() <= 21 and dealer.get_hand_value() > 21: # dealer busts
            return "Player"
        elif player.get_hand_value() <= 21 and dealer.get_hand_value() <= 21: # neither bust
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
    deck.build(deck_template_standard, 5)
    deck.shuffle()

    # Create the players/Dealer
    dealer = Player("Dealer")
    player = Player("Player1")
    
    # The game begins!
    # Both, the player and the dealer draw 2 cards.
    player.draw_card(deck)
    dealer.draw_card(deck)
    player.draw_card(deck)
    dealer.draw_card(deck)

    # Reveal the drawn cards, 2 for the player and an upcard for the dealer
    player.show()
    dealer.show_card()

    # Decision time, based on the drawn and shown cards
    # if dealer.get_card().get_value() == 11:
    #     # offer insurance
    if player.get_hand_value() == 21:
        # also need to implement insurance for here
        if dealer.get_hand_value() == 21:
            pass
        else:
            while dealer.get_hand_value() < 21:
                dealer.draw_card(deck)
    elif player.get_hand_value() < 21:
        if dealer.get_card(0).get_value() == 11:
            # offer insurance
            print('would offer insurance to you but o well.')
            if dealer.get_hand_value() == 21:
                pass # exit this logic and evaluate the hands. the player should lose
        if dealer.get_hand_value() < 21:
            response = None
            disable_double = False
            while player.get_hand_value() < 21 and response != '3':
                if disable_double == False:
                    response = input("(1) hit, (2) double, (3) stand: ")# also need to incorporate splitting at some point.
                    if response == '2':
                        player.draw_card(deck)
                        player.show()
                        break
                else:
                    response = input("(1) hit or (3) stand: ") 
                if response == '1':
                    disable_double = True
                    player.draw_card(deck)
                    player.show()
            if player.get_hand_value() > 21: # the dealer does not hit if the player busts
                pass
            else:
                # Dealer's turn. Dealer hits soft serves
                while dealer.get_hand_value() <= 17:
                    if dealer.get_hand_value() == 17:
                        if dealer.find_card('Ace') == True:
                            dealer.draw_card(deck)
                        else:
                            break
                    if dealer.get_hand_value() < 17:
                        dealer.draw_card(deck)
                        print({dealer.show()})
                    else: 
                        print("how did I get here? where am i? who are you?")
                        break

    print("~~~~~ Final Hands ~~~~~")        
    player.show()
    dealer.show()

    print(evaluate_winner(player, dealer))

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