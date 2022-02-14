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
me = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if me == '0':
  print(rock)
elif me == '1':
  print(paper)
elif me == '2':
  print(scissors)

computer = str(random.randint(0, 2))

if me == computer:
  print("Computer Chose:\n")
  if computer == '0':
    print(rock)
  elif computer == '1':
    print(paper)
  elif computer == '2':
    print(scissors)
  print("Game Tied!")
elif int(me) > 2 or int(me) < 0:
  print("This is an invalid number!")
else:
  print("Computer Chose:\n")
  if me == '0' and computer == '1':
    print(paper)
    print("You Lost!")
  elif me == '0' and computer == '2':
    print(scissors)
    print("You Won!")
  elif me == '1' and computer == '0':
    print(rock)
    print("You Won!")
  elif me == '1' and computer == '2':
    print(scissors)
    print("You Lost!")
  elif me == '2' and computer == '0':
    print(rock)
    print("You Lost!")
  elif me == '2' and computer == '1':
    print(paper)
    print("You Won!")

