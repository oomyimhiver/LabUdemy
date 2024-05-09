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
game_images = [rock, paper, scissors]
#Write your code below this line 👇
import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice<0 or user_choice>2:
  print("You typed an invalid number, you lose!")
else:
  print(game_images[user_choice])

  computer_choice = random.randint(0,2)
# if user_choice == 0:
#   print(rock)
# if user_choice == 1:
#   print(paper)
# if user_choice == 2:
#   print(scissors)
  print("Computer chose:")
  print(game_images[computer_choice])
# if computer_choice == 0:
#   print(rock)
# if computer_choice == 1:
#   print(paper)
# if computer_choice == 2:
#   print(scissors)

  if user_choice == 0 and computer_choice == 0:
    print("It's a draw")
  if user_choice == 0 and computer_choice == 1:
    print("You lose")
  if user_choice == 0 and computer_choice == 2:
    print("You win")
  if user_choice == 1 and computer_choice == 0:
    print("You win")
  if user_choice == 1 and computer_choice == 1:
    print("It's a draw")
  if user_choice == 1 and computer_choice == 2:
    print("You lose")
  if user_choice == 2 and computer_choice == 0:
    print("You lose")
  if user_choice == 2 and computer_choice == 1:
    print("You win")
  if user_choice == 2 and computer_choice == 2:
    print("It's a draw")
