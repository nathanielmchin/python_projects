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