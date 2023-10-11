########### Python Loops ############

# For loop in lists
# for items in list_of_items:
#     Do something to each item

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
    
# here we loop through the fruits list (array in js)
# coding challenge1
# Coding Challenge 2

# using for loop with the range
# for number in range(a, b):
#       print(number)

for number in range(1, 10):
    print(number)
# here we get a list of numbers fron 1 - 10

for number in range(1, 11, 3):
    print(number)
# here we get a list of numbers from 1 - 11 skipping 3. 1, 4, 7, 10 

total = 0
for number in range(1, 101):
    total += number
    
# Coding Challenge 3

# Coding Challenge 4