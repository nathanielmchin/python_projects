class Card():
    def __init__(self, code, suit, value):
        self._code = code
        self._suit = suit
        self._value = value
    
    # Code: AS (ace of spade)
    def get_code(self):
        return self._code
    # Suit: Spades
    def get_suit(self):
        return self._suit
    # Value: Ace
    def get_value(self):
        return self._value
    

class Deck():
    # Decks loop through value of 1-10, 10 3 times for J Q K 
    # Suits Represented as C - H - S - D for [CLUBS, HEARTS, SPADES, DIAMONDS]
    # Cards represented as Value first then Suit [2S = 2 of Spades, AD = Ace of Diamonds]
    def __init__(self, Joker=False):
        self._cards = []
        self.build()

    def build(self):
        for suit in ['C','H','S','D']:
            for num in range(1,11):
                if num == 1:
                    num = 'A'
                else:
                    num = str(num)
                code = suit + num
                card = Card(code, suit, num)
                self._cards.append(card)

            for num in ['J','Q','K']:
                code = suit + num
                card = Card(code, suit, num)
                self._cards.append(card)
