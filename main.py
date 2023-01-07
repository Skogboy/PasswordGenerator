
import random
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


p_letter = ''
p_number = ''
p_symbols = ''

for n in range(0, nr_letters):
  ra_letters = random.randint(0, 51)
  
  p_letter += letters[ra_letters]

  
for n in range(0, nr_symbols):
  ra_symbols = random.randint(0, 8)
  
  p_symbols += symbols[ra_symbols]



for n in range(0, nr_numbers):
  ra_numbers = random.randint(0, 9)
  
  p_number += numbers[ra_numbers]


print(f"Your new password is {p_letter}{p_symbols}{p_number}")

random_password = p_letter + p_symbols + p_number

l = list(random_password)
random.shuffle(l)
result = ''.join(l)
print(f'Your new random password is {result}')
  