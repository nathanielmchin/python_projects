import random

# Define card values
card_values = {
    'Ace': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 0,
    'Jack': 0,
    'Queen': 0,
    'King': 0
}

# Define function to deal a card
def deal_card():
    card = random.choice(list(card_values.keys()))
    return card, card_values[card] 

# Define function to determine the winner
def determine_winner(player_total, banker_total):
    if (player_total > banker_total):
        return 'Player'
    elif (player_total < banker_total):
        return 'Banker'
    else:
        return 'Tie'

def calculate_total(user_cards):
    total = sum(card[1] for card in user_cards) % 10
    return total

# Play a game of Baccarat
def play_baccarat():
    # Deal two cards to the player and two cards to the banker
    player_cards = [deal_card() for i in range(2)]
    banker_cards = [deal_card() for i in range(2)]

    # First phase of calculation    
    player_total = calculate_total(player_cards)
    banker_total = calculate_total(banker_cards)

    # Determine if a 3rd card needs to be dealt
    # Player is evaluated first
    if player_total < 5 and banker_total < 8:
        player_cards += [deal_card()]
    
    # Now it's the Banker's turn
    if banker_total < 3 and player_total < 8:
        banker_cards += [deal_card()]
    elif len(player_cards) < 3 and banker_total < 7:
        banker_cards += [deal_card()]
    elif banker_total == 3 and player_cards[2][1] != 8:
        banker_cards += [deal_card()]
    elif banker_total == 4 and player_cards[2][1] not in [1,8,9,10]:
        banker_cards += [deal_card()]
    elif banker_total == 5 and player_cards[2][1] not in [1,2,3,8,9,10]:
        banker_cards += [deal_card()]
    elif banker_total == 5 and player_cards[2][1] not in [1,2,3,4,5,8,9,10]:
        banker_cards += [deal_card()]

    if len(player_cards) == 3 or len(banker_cards) == 3:
        player_total = calculate_total(player_cards)
        banker_total = calculate_total(banker_cards)

    winner = determine_winner(player_total, banker_total)
    
    results = {
        'Players_cards' : player_cards,
        'Players_total' : player_total,
        'Bankers_cards' : banker_cards,
        'Bankers_total' : banker_total,
        'Winner' : winner
    }
    
    return results

def simulate_strategy_ftl(player_total, wager_base, wager_multiplier, simulation_count):
    player_total        = player_total
    wager_base          = wager_base
    wager_multiplier    = wager_multiplier
    simulation_count    = simulation_count
    
    banker_wins_total = 0
    player_wins_total = 0
    ties_total = 0

    game_history = []
    bet_on = 'Player'

    for i in range(simulation_count):
        wager = wager_base * wager_multiplier
        payout = 0
        
        game_results = play_baccarat()
        game_history = game_results
        winner = game_results['Winner']

        # Set payouts based on the winner and increment the win/lose stats
        if winner == 'Player':
            player_wins_total += 1
            payout = wager
        elif winner == 'Banker':
            banker_wins_total += 1
            payout = wager * .95
        else:
            ties_total += 1
            payout = wager * 8
        
        # Add (or subtract) the payouts and modify the wager based on the player's accuracy
        if winner == bet_on:
            player_total += payout
            wager_multiplier -= 1
            if wager_multiplier < 3:
                wager_multiplier = 5
        elif winner == 'Tie':
            pass
        else:
            player_total -= wager
            wager_multiplier = 5

        # Follow the leader! Change bet to the the new winner. If the winner was 'tie', stay the course
        if winner != 'Tie':
            bet_on = winner

    results = {
        'GameHistory'   : game_history,
        'PlayerWins'    : player_wins_total,
        'BankerWins'    : banker_wins_total,
        'Ties'          : ties_total,
        'PlayerTotal'   : player_total
    }
    return results

simulation = simulate_strategy_ftl(1000, 25, 5, 100)
# print(f"{simulation['GameHistory']}")
print(f"Player Wins  = {simulation['PlayerWins']}")
print(f"Banker Wins  = {simulation['BankerWins']}")
print(f"Ties         = {simulation['Ties']}")
print(f"Player Total = {simulation['PlayerTotal']}")