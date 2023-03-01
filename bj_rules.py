def get_values(hand):
    # Returns both soft and hard values
    # If no ace, both will be the same
    # [Soft, Hard]
    val = [0,0]
    for card in hand:
        if card == 'A':
            val[0] += 1 
            val[1] += 11
        elif card in ['J','Q','K']:
            val = list(map(lambda x: x + 10, val))
        else: 
            c_val = int(card)
            val = list(map(lambda x: x + c_val, val))
    return val

def highest_val(values):
    if values[1] <= 21:
        return values[1]
    return values[0]