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

#Write your code below this line 👇
options = [rock, paper, scissors]

me = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if me > 2:
  print("Invalid option has been selected!")
else:
  print(options[me])
  computer = random.randint(0, 2)
  if options[me] == options[computer]:
    print("Computer Chose:\n")
    print(options[computer])
    print("Game Tied!")
  else:
    win_statement = "You Won!"
    lose_statement = "You Lost!"
    print("Computer Chose:\n")
    print(options[computer])
    if me == 0 and computer == 1:
      print(lose_statement)
    elif me == 0 and computer == 2:
      print(win_statement)
    elif me == 1 and computer == 0:
      print(win_statement)
    elif me == 1 and computer == 2:
      print(lose_statement)
    elif me == 2 and computer == 0:
      print(lose_statement)
    elif me == 2 and computer == 1:
      print(win_statement)