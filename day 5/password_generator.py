####################### Password Generator ##########################
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", 
           "w", "x", "y", "z", "A", "B", "C", "D", "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like\n"))
nr_numbers = int(input(f"How many numbers would you like\n"))

password = []

for password in range(1, nr_letters + 1):
    random1 = random.choice(letters)
    password.append(random1)
    

for symbol in range(1, nr_symbols + 1):
    random2 = random.choice(letters)
    password.append(random2)
    
    

for number in range(1, nr_numbers + 1):
    random3 = random.ranint(1, nr_letters - 1)
    # number_password += numbers[random3]
    password.append(random3)
   

shuffled = ""

for word in range(1, len(password) + 1):
    random4 = random.ranint(1, len(password) - 1)
    shuffled += password[random4]
 
 
print(shuffled)   
    
# OR

random.shuffle(password)

password_final = ""
for char in password:
    password_final += char

print(password_final)
    