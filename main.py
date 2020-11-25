############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


from art import logo


print("May the odds ever be in your favor!")
print("Let's deal!")

#draw card 
def draw_card(user_hand):
  """Returns a random card from the deck."""
  card = random.randint(0,12)
  user_hand.append(cards[card])


#Adds cards in hand
def calculate_score(user_hand):
  score = sum(user_hand)
  #Checks for blackjack in 2 cards
  if len(user_hand) == 2 and score == 21:
    return 0

  #Checks for ace and > 21
  if 11 in user_hand and score > 21:
    user_hand.remove(11)
    user_hand.append(1)  
  return score

#Comparing scores
def compare(player_score, dealer_score):
  if player_score == dealer_score:
    return "Draw"
  elif dealer_score == 0:
    return "Lose, opponent has Blackjack"
  elif player_score == 0:
    return "Win, you have Blackjack!"
  elif player_score > 21:
    return "You went over.  You lose."
  elif dealer_score > 21:
    return "Oppenent busted.  You win!"
  elif player_score > dealer_score:
    return "You win!"
  else:
    return "You lose."

def play_game():
  dealer_cards = []
  player_cards = []
  is_game_over = False
  print(logo)
  #Starting Hands
  for _ in range(2):
    draw_card(player_cards)
    draw_card(dealer_cards)

  #This loop runs when player wants to keep drawing cards
  while not is_game_over:
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Dealer's card: {dealer_cards[0]}")

    if player_score == 0 or dealer_score == 0 or player_score > 21:
      is_game_over = True

    else:
      player_should_deal = input("Type 'h' for a hit or 's' to stay:  ")
      if player_should_deal == 'h':
        draw_card(player_cards)
      else:
        is_game_over = True

  #Dealer strategy
  while dealer_score != 0 and dealer_score < 17:
    draw_card(dealer_cards)
    dealer_score = calculate_score(dealer_cards)
    print(dealer_score)
    print(dealer_cards)

  print(f"Your final hand was {player_cards}, final score: {player_score}")
  print(f"Dealer's final hand was {dealer_cards}, final score: {dealer_score}")
  print(compare(player_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ") == 'y':
  clear()
  play_game()

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

