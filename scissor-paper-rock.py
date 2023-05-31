import random 

def get_choices():
  player_choice = input("Enter a choice(rock, paper, scissors: )")
  options = ['rock', 'paper', 'scissors']
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player} and computer chose {computer}")
  if player == computer:
    return ("it's a Tie!")
  elif player == "rock": 
    if computer == "scissors":
      return ("Rock smashes scissors, you win")
    else:
      return("Paper Cover Rock, you lose")
  elif player == "paper":
    if computer == "rock":
      return ("Paper cover rock, you win")
    else:
      return ("Scissors cut paper, you lose")
  elif player == "scissors":
    if computer == "paper":
      return("Scissors cut paper, you win")
    else:
      return("Rock kills scissors, you lose")

choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)