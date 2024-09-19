import random

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