me = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if me == '0':
  print(rock)
elif me == '1':
  print(paper)
elif me == '2':
  print(scissors)

print("Computer Chose:\n")
computer = str(random.randint(0, 2))
if computer == '0':
  print(rock)
elif computer == '1':
  print(paper)
elif computer == '2':
  print(scissors)

if me == computer:
  print("Game Tied!")
else:
  if me == '0' and computer == '1':
    print("You Lost!")
  elif me == '0' and computer == '2':
    print("You Won!")
  elif me == '1' and computer == '0':
    print("You Won!")
  elif me == '1' and computer == '2':
    print("You Won!")
  elif me == '2' and computer == '0':
    print("You Lost!")
  elif me == '2' and computer == '1':
    print("You Won!")