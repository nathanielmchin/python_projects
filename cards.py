import random
class Card():
    def __init__(self, code, suit, value):
        self._code = code
        self._suit = suit
        self._value = value

    # Code: AS
    def get_code(self):
        return self._code
    # Suit: Spades
    def get_suit(self):
        return self._suit
    # Value: A
    def get_value(self):
        return self._value
    
    
    # Neat: Ace of Spades
    def show_neat(self): 
        val_dict = {
            'A': 'Ace',
            'J': 'Jack',
            'Q': 'Queen',
            'K': 'King'
        }
        suit_dict = {
            'S': "Spades",
            'H': "Hearts",
            'C': "Clubs",
            'D': "Diamonds",
        }

        val = self._value
        if self._value in ['A','J','Q','K']:
            val = val_dict[self._value]
        
        return val + " of " + suit_dict[self._suit]
class Deck():
    # Cards represented as Value first then Suit [2S = 2 of Spades, AD = Ace of Diamonds]
    def __init__(self, size_of_deck=1, Joker=False):
        self._cards = []
        self.build(size_of_deck)

    def build(self, loop):
        for i in range(loop):
            for suit in ['S','H','C','D']:
                for num in range(1,11):
                    if num == 1:
                        num = 'A'
                    else:
                        num = str(num)
                    code = num + suit
                    card = Card(code, suit, num)
                    self._cards.append(card)

                for num in ['J','Q','K']:
                    code = num + suit
                    card = Card(code, suit, num)
                    self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)