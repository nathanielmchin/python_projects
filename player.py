# Player made for Black jack - for now only 1 hand
class Player(): 
    def __init__(self, name):
        self._name = name
        self._hand = []
        self._val = []

        self._suitless_hand = []
        # # Eventually need to add below
        # self._bank = 0

    def show_hand(self):
        show = []
        for card in self._hand:
            show.append(card.show_neat())
        print(show)

    def add_card(self, card):
        self._hand.append(card)
        self._suitless_hand.append(card._value)
        
    def show_top(self):
        show = []
        show.append(self._hand[0].show_neat())    
        show.append("-----------")
        print(show)