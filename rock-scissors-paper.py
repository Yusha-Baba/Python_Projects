player_1 = input()
player_2 = input()
if player_1 == "rock" and player_2 == "scissors":
  print("Player 1 wins")
elif player_1 == "paper" and player_2 == "rock":
  print("Player 2 wins")
elif player_1 == "scissors" and player_2 == "paper":
  print("Player 1 wins") 
else:
  print("Not Valid -No cheating")
