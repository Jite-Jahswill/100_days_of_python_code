import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

# Rock wins against sissors
# scissors win against paper
# paper wins against rock.

rock = '''
    _______
---'    ___)
       (___)
       (___)
       (__)
----.__(_)
'''
paper = '''
    _______
---'    ___)____
       (________)
       (_________)
       (________)
----.__(______)
'''
scissors = '''
    _______
---'    ___)______
       (__________)
       (__________)
       (__)
----.__(_)
'''

out_come = [rock, paper, scissors]
if choice >= 3:
    print("Invalid input please try again following instructions")
elif choice >= 0 <= 3:
    print(out_come[choice])

computer = print("Computer chose: ")
random = random.randint(0 ,2)
print(out_come[random])

if choice == 0 and computer == 2:
        print("You Win")
elif choice == 2 and computer == 1:
        print("You Win")
elif choice == 1 and computer == 0:
        print("You win")
elif choice == computer:
    print("Its a draw")
else:
    print("you loose")