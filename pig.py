import random

max_score = 50

#####METHODS####################################
def roll():
  min_val = 1
  max_val = 6
  roll = random.randint(min_val, max_val)
  
  return roll

######GAME INITIALIZATION########################
while True:
  players_count = input("Enter the number of players (2-4): ")
  if players_count.isdigit():
    players_count = int(players_count)
    if 2 <= players_count <= 4:
      break
    else:
      print("Selection must be betweeen 2 and 4 players. Please make a valid choice.")
  else:
    print()

# initialize players count list w/ 0 value for each player created
player_scores = [0 for p in range(players_count)]

while max(player_scores) < max_score:
  # START TURN
  for player_i in range(players_count):
    print("\nPlayer", player_i + 1, "turn has just started!")
    print("Your total score is;", player_scores[player_i], "\n")
    current_score = 0
    
    while True:
      should_roll = input("Would you like to roll (y)?: ").lower()    
      if should_roll != "y":
        break

      value = roll()

      if value == 1:
        print("You rolled a 1, now your turn is done!!")
        current_score = 0
        break
      else:
        current_score += value
        print("You rolled a:", value)
      
      print("Your wcore is:", current_score)

    player_scores[player_i] += current_score
    print("Your total score is:", player_scores[player_i])
  print('Player number', player_i, "turn is now over. ")
#end max_score while loop check

#winning conditions & program end
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print('Player', winning_idx + 1, "is the winner with a score of:", max_score)