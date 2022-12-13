import random

# Add betting

player_cards = []
dealer_cards = []

while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print(f"\nDealer's hand: {dealer_cards} = {sum(dealer_cards)}")
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print(f"Your Hand: {player_cards} = {sum(player_cards)}")
while sum(player_cards) < 21:
    option = input("\nH: Hit\nS: Stand\n")
    if option.lower() == 'h':
        # Add Ace high/low option
        player_cards.append(random.randint(1, 11))
        print(f"Your Hand: {player_cards} = {sum(player_cards)}")
    if option.lower() == 's':
        print(f"\nStood at: {sum(player_cards)}")
        while sum(dealer_cards) < 17 and sum(dealer_cards) < sum(player_cards):
            dealer_cards.append(random.randint(1, 11))
            print(f"Dealer's hand: {dealer_cards} = {sum(dealer_cards)}")
        if sum(dealer_cards) > sum(player_cards) and sum(dealer_cards) < 21:
            print("\nYou lost")
            break
        elif sum(dealer_cards) == sum(player_cards):
            print("\nDraw")
            break
        else:
            print("\nYou won")
            break
if sum(player_cards) == 21 and sum(dealer_cards) == 21:
    print("Draw")
elif sum(dealer_cards) == 21:
    print("Dealer Blackjack")
elif sum(player_cards) == 21:
    print("Player Blackjack")
# if sum(dealer_cards) > 21:
#     print("\nDealer Busted")
if sum(player_cards) > 21:
    print("\nYou Busted")