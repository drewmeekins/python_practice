# rock paper scissors game

# Hides input from each player
# from getpass import getpass as input



print("Let's play Rock Paper Scissors!")

player_1_move = input("Player 1, select Rock, Paper, or Scissors as a move: ")
player_2_move = input("Player 2, select Rock, Paper, or Scissors as a move: ")

# Rock
if player_1_move == "Rock" and player_2_move == "Rock":
    print(f"Draw! Player 1 selected {player_1_move} and Player 2 selected {player_2_move}")
elif player_1_move == "Rock" and player_2_move == "Scissors":
    print(f"Player 1 Wins! Player 1 selected {player_1_move} and Player 2 selected {player_2_move}")
elif player_1_move == "Rock" and player_2_move == "Paper":
    print(f"Player 2 Wins! Player 2 selected {player_2_move} and Player 2 selected {player_1_move}")
# Paper
elif player_1_move == "Paper" and player_2_move == "Paper":
    print(f"Draw! Player 1 selected {player_1_move} and Player 2 selected {player_2_move}")
elif player_1_move == "Paper" and player_2_move == "Rock":
    print(f"Player 1 Wins! Player 1 selected {player_1_move} and Player 2 selected {player_2_move}")
elif player_1_move == "Paper" and player_2_move == "Scissors":
    print(f"Player 2 Wins! Player 2 selected {player_2_move} and Player 2 selected {player_1_move}")
# Scissors
elif player_1_move == "Scissors" and player_2_move == "Scissors":
    print(f"Draw! Player 1 selected {player_1_move} and Player 2 selected {player_2_move}")
elif player_1_move == "Scissors" and player_2_move == "Paper":
    print(f"Player 1 Wins! Player 1 selected {player_1_move} and Player 2 selected {player_2_move}")
elif player_1_move == "Scissors" and player_2_move == "Rock":
    print(f"Player 2 Wins! Player 2 selected {player_2_move} and Player 2 selected {player_1_move}")
else:
    print(f"Player 2 Wins! Player 2 selected {player_2_move} and Player 2 selected {player_1_move}")

