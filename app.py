# write 'hello world' to the console
#print('hello world')
#Source: GEMINI *STAR

import random

# Game options
options = ["rock", "paper", "scissors"]

def play_round(player_choice):
  """
  Plays a single round of Rock-Paper-Scissors against the computer.

  Args:
    player_choice: The player's choice of rock, paper, or scissors.

  Returns:
    A string indicating the winner of the round, or "Tie" if the round is tied.
  """

  # Get computer's choice
  computer_choice = random.choice(options)

  # Determine winner
  if player_choice == computer_choice:
    return "Tie"
  elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
    return "Win"
  else:
    return "Lose"

def main():
  """
  The main function of the Rock-Paper-Scissors game.
  """

  player_score = 0
  rounds_played = 0

  while True:
    # Get player's choice
    player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()

    if player_choice == "quit":
      break
    elif player_choice not in options:
      print("Invalid choice. Please enter rock, paper, or scissors.")
      continue

    # Play a round
    result = play_round(player_choice)
    rounds_played += 1

    if result == "Win":
      player_score += 1
      print("You win!")
    elif result == "Lose":
      print("You lose.")
    else:
      print("It's a tie!")

    # Ask player if they want to play again
    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
      break

  # Print final score
  print(f"You won {player_score} out of {rounds_played} rounds.")

if __name__ == "__main__":
  main()