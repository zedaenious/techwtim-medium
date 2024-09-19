import random

max_score = 50

def roll():
  min_val = 1
  max_val = 6
  roll = random.randint(min_val, max_val)
  
  return roll

while True:
  players = input("Enter the number of players (2-4): ")
  if players.isdigit(): #gasp! errror handling
    players = int(players)
    if 2 <= players <= 4:
      break
    else:
      print("Selection must be betweeen 2 and 4 players. Please make a valid choice.")
  else:
    print()

player_scores = [0 for p in range(players)]

print(player_scores)

while max(player_scores) < max_score:
  current_score = 0
  should_roll = input("Would you like to roll (y)?: ").lower()
  
  if should_roll != "y":
    break

  value = roll()

  if value == 1:
    print("You rolled a 1, now your turn is done!!")
    break
  else:
    current_score += value
    print("You rolled a:", value)
  
  print("Your wcore is:", current_score)
