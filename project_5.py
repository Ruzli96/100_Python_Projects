#Password Generator Project
import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
		  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
		  'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 
		  'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
		  'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
myList = []
for count in range(nr_letters):
	char = random.choice(letter)
	myList.append(char)

for count in range(nr_symbols):
	char = random.choice(symbols)
	myList.append(char)

for count in range(nr_numbers):
	char = random.choice(numbers)
	myList.append(char)

random.shuffle(myList)
print(password.join(myList))