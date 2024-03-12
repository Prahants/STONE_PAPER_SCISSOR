import random 

def display_choices():
  print("1. Stone")
  print("2. Paper")
  print("3. Scissor")
  print("4. Quit")

def determine_winner(player_choice, computer_choice):
  if player_choice == computer_choice:
    return "Tie"
  elif (player_choice == 1 and computer_choice == 3) or \
       (player_choice == 2 and computer_choice == 1) or \
       (player_choice == 3 and computer_choice == 2):
    return "You win :-) "
  else:
    return "Computer wins :-( "

game_list = ["Stone", "Paper", "Scissor"]
computer_point = 0
player_point = 0
print(f"Score: Computer {computer_point}, Player {player_point}")

while True:
  display_choices()
  choice = int(input("Enter your choice: "))

  if choice == 4:
    break

  computer_choice = random.randint(1, 3)
  print("Computer's choice:", game_list[computer_choice -1 ])

  result = determine_winner(choice, computer_choice)
  print(result)

  # Update scores based on the result
  if result == "You win :-) ":
    player_point += 1
  elif result == "Computer wins :-( ":
    computer_point += 1


  print(f"Score: Computer {computer_point}, Player {player_point}")

print(f"Final Score: Computer {computer_point}, Player {player_point}")
