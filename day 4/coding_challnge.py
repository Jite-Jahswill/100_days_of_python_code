# Coding challenge 1

# Instructions
# You are going to write a virtual coin toss program. it will randomly tell the user "heads" or "tails".
# Important, the first letter should be capitalized and spelt exactly like in the example e.g Heads, not heads.
# There are many ways of doing this. But to practice what we learnt in the slast lesson, you should generate a rando number,
# either 0 or 1. Then use that number to print out Heads or Tails
# 
# e.g.
# 1 means Heads
# 0 means Tails


# Write your code below
# Hint: Remember to import the random module first.

import random

out_come = random.randint(0, 1)

if out_come == 0:
    print("Tails")
else:
    print("Heads")
    
# coding Challenge 2
# Whose Paying

# Instructions 
# Your are going to write a program which will select a random name from a list of names. The person selected
# will have to pay for everybody's food bill. Important: You are not allowed to use the choice() function.
# Line 8 splits the string name_string into individual names and puts them inside a list called names. for this to work, you must
# enter all the names as name followed by comma then spae. e.g. name, name, name
# 
# Hint
# You might need the len() function
# 
# Split string method
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
# Dont change this code

# write your code here
new_name = len(names)

out_come = random.randint(0, new_name - 1)

print(names[out_come])

# or
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the mesl today.")

# Coding Challenge 3

# Intructions
# you are going to write a program which with mark a spot with X.
# the map is made of 3 rows of blank squares.
#   1  2  3
# 1["","",""]
# 2["","",""]
# 3["","",""]
# 
# Your program should allow you to enter the position of the treasure using a two-digit system.
# The first digit is the horizontal column number and the second digit is the vertical row number. e.g.
# 
# Dont change the code below
# 
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position =input("where do you want to put the treasure? ")

# write your code here
# splitting our input
horizonal = int(position [0])
vertical = int(position [1])

selected_row = map[vertical - 1]
selected_row[horizonal - 1] = "❌"
# or
map[vertical - 1][horizonal - 1] = "❌"

# dont change this code
print(f"{row1}\n{row2}\n{row3}")