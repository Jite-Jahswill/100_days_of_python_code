# Coding challenge 1 day 3.1

# Instructions 
# write a program that works out whether if a given number is an odd or even number. Even numbers can be divided by 2 with no remainder
# e.g. 86 is even because 86 / 2 = 43 43 does not have any decimal places. therfore the division is clean.
# e.g 59 is odd because 59 / 2 = 36.875 36.875 is not a whole number, it has decimal places. Therefore there is remainder of 0.875,
# so division is not clean.
# The modulo is written as percentage sign(%) in pythom. it gives you the remainder after a division
# e.g. 6 / 2 = 3 with no remainder., 6 % 2 = 0, 5 / 2 = 2 * 2 + 1, remainder is 1, 5 % 2 = 1

# dont change the code below
number = int(input("Which number do you want to check? "))

# write your code here

check = number % 2

if check == 0:
    print("This is an even number")
else:
    print("This is an odd number")
    
# Coding Challenge 2 day 3.2

# Instructions
# Write a program that interprets the Body Mass Index(BMI) based on a user's weight and height.
# it should tell them the interpretation of their BMI based on the BMI value.
# under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese
# The BMI is calculated by dividing a persons weight (in KG) by the square of their height (in m).
# BMI = weight(Kg)/ height²(m²)

# warning you should convert the result to a whole number. The interpretation message needs to include the words in bold
# from the interpretations above e.g. Underweight, normal weight, overweight, obese, clinically obese.

# Dont change the code

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# write your code here
new_weight = int(weight)
new_height = int(float(height) * float(height))

BMI = int(new_weight / new_height)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight")
elif 18.5 <= BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight")
elif 25 <= BMI < 30:
    print(f"Your BMI is {BMI}, you are overweight")
elif 30 <= BMI < 35:
    print(f"Your BMI is {BMI}, you are obese")
else:
    print(f"Your BMI is {BMI}, you are clinically obese")


# Coding Challenge

# write a program that works out whether if 
# a given year is a leap year and normal year is 365 
# Days leap years have 666 need an extra in Friday 
# the reason why we have leap years is really fascinating 
# this video does it  justice  https://www.youtube.com/watch?v=xX96xng7sAE
# this is how we work out whether if a particular year is a leap year  
# on every year that is evenly divisible by 4 
# except every year that is evenly divisible by 100 
# unless the year is also evenly divisible by 400  
# e.g  example  the year 2000  
# 2000 / 4 = 500 (leap year)
# 2000 / 100 equals 20 (not leap year)
# 2000 / 400 equals 5 (leap year)  
# so the year 2000 is a leap year 
# but the Year 2100 is not a leap year because 
# 2100 / 4 give us 525(leap) 
# 2100 ÷ 100 equals 21 (leap)
# 2100 / 400 give us 5.25(not leap) 
# 2100 is not a leap year

year = int(input("Please insert a year "))

year = 2023

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# coding Challenge 3

# congratulations on a job at Python pizza Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill. 
# Small pizza: $15 
# medium pizza: $20 
# large pizza: $25 
# pepperoni for small pizza: +$2 
# pepperoni for medium or large pizza: +$3 
# extra cheese for any size pizza: +$1

# Dont change the code below
print('Welcome to Python Pizza!')
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

price = 0

if size == "S":
    price += 15
    if add_pepperoni == "Y":
        price += 2
if size == "M":
    price += 20
    if add_pepperoni == "Y":
        price += 3
if size == "L":
    price += 25
    if add_pepperoni == "Y":
        price += 3
if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}.")

# Coding challenge 4

# you are going to write a program that test  
# the compatibility between two people we are going to use 
# the super scientific method recommended by BuzzFeed the workout the love score 
# between two people take both people's names and check for the number of times the 
# letters in the word true occur then check for the number of times the letter occurs in 
# the world love of course then combine these numbers to make a two digit number
# for love scores less than 10 or greater than 90, the message should be:
# "Your score is x, you go together like coke and mentos."
# for love scores lis between 40 or greater than 50, the message should be:
# "Your score is x, you are allright together."
# otherwise the message should just be their score. e.g,
# "your score is z"

# HINTS
# 1. The lower() function changes all the letters in a string to lower case.
# 2. The count() function will give you the number of times a letter occurs in a string

# e.g. 
# name1 = "Angela Yu"
# name2 = "Jack Bauer"

# T occurs 0 times
# R occurs 1 times
# U occurs 2 times
# E occurs 2 times
# Total = 5

# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3

# Love Score = 53
# Print: "Your score is 53."

# Dont change the code below
print('Welcome to the Love Calculator!')
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

# Write your code below this line
true_count = name1.count("t") + name2.count("t") + name1.count("r") + name2.count("r") + name1.count("u") + name2.count("u") + name1.count("e") + name2.count("e")
love_count = name1.count("l") + name2.count("l") + name1.count("o") + name2.count("o") + name1.count("v") + name2.count("v") + name1.count("e") + name2.count("e")

love_score = int(str(true_count) + str(love_count))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
