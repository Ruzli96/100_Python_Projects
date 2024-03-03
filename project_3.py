# Takes string commands to journey through and locate the treasure

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("Which direction would you like to go? Type 'left' or 'right'\n")
if direction != "left":
  print("You fell into a hole. Game Over.")
else:
  travel = input("You have arrived at a lake and there is an island in a distance. Type 'wait' to wait\
  for a boat. Type 'swim' to swim across.\n")
  if travel != "wait":
    print("You have been attacked by a trout. Game Over.")
  else:
    door_color = input("You have arrived safely to the island. There is a barn with 3 doors. Type 'red', 'yellow', or 'blue' to choose a door\n")
    if door_color == "red":
      print("You have been burnt by fire. Game over.")
    elif door_color == "blue":
      print("You have been eaten by beasts. Game Over.")
    elif door_color == "yellow":
      print("You Win!")
    else:
      print("Game Over.")