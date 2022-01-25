import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# Collection of items
game_options = [rock, paper, scissors]

# user choice
user_choice = int(input("What would you like to choose? Type 0 = Rock, 1 = Paper, 2 = Scissors.\n"))
print(game_options[user_choice])

pc_choice = random.randint(0, 2)
print("Is the time for the PC:")
print(game_options[pc_choice])


if user_choice >= 3 or user_choice < 0:
  print("You typed the wronf number, you will loose!")
elif user_choice == 0 and pc_choice == 2:
  print("You win!")
elif pc_choice == 0 and user_choice == 2:
  print("You lose")
elif pc_choice > user_choice:
  print("You lose")
elif user_choice > pc_choice:
  print("You win!")
elif pc_choice == user_choice:
  print("It's a draw")



