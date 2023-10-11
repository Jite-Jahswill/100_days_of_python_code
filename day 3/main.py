# Conditional Statements, logical operators, code blocks and scope

# Conditional statement can be seen as a method of controlling water overflow in bathtub they checkmate stuff
## if condition:
##     do this
## else:
##     do this

water_level = 50
if water_level > 80:
    print("Drain Water")
else:
    print("Continue")
    
# Another example 
    
print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")
    
# if u misplace the stament in the if by removing the indentation you'll get an indent error

# Comparison operators include > greater than < lesser than >= greater than or equal to 
# <= lesser than or equal to == equal to != not equal to
# Coding challenge 1


# Nested if else statements. here once the first condition is passed we can check for another e.g.
## if condition :
##    if another condition:
##        do this
##    else:
##        do this
## else: 
##    do this

# the example above is a nested if statement

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("please pay $7.")
    else:
        print("please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# what if we have more than two conditions we can use if / elif / else e.g.
## if condition1:
##      do A
## elif condition2:
##      do b
## else:
##      do this

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("please pay $5.")
    elif age <= 18:
        print("please pay $7.")
    else:
        print("please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
    
# we can keep going with elif till we are satisfied with our conditions.
# coding Challenge 2


# Multiple if conditions
# if condition1:
#     do 1
# if condition2:
#     do 2
# if condition3:
#     do 3

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Children pay $5.")
    elif age <= 18:
        bill = 7
        print("Youth pay $7.")
    else:
        bill = 12
        print("Adults pay $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
# coding Challenge 3

# checking for multiple conditions 
# if condition 1 & condition 2 & condition 3:
#     do this
# else:
#     do this

# we can do this only using logical operators and, or with not. when we use and we get true or flase
print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Children pay $5.")
    elif age <= 18:
        bill = 7
        print("Youth pay $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("You earned a free ride.")
    else:
        bill = 12
        print("Adults pay $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")