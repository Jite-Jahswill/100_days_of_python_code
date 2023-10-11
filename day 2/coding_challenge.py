# Challenge 1 Datatypes

# Instructions: write a program that adds the digits in a 2 digit number. e.g. if the input
# was 35, then the output should be 3 + 5 = 8

# Dont change this code
two_digit_number = input("Type a two digit number: ")

# Write Your code here

addition = int(two_digit_number[0]) + int( two_digit_number[1])

print(addition)



# Challenge 2 BMI Calculator
# write a program that calculates the Bofy Mass Index (BMI) fro a user's weigth and height.

# The BMI is a measure of someones weight taking into account their height. e.g. if a tall 
# person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a persons weight (in KG) by the square of their height (in m).
# BMI = weight(Kg)/ height²(m²)

# warning you should convert the result to a whole number.

# Dont change the code

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# write your code here
new_weight = int(weight)
new_height = int(float(height) * float(height))

BMI = new_weight / new_height

print(int(BMI))


# Chalenge 3 Your life in weeks
# Instructions I was reading this articulr by Tom Urban - Your life in weeks and I realised just how
# little time we actually have.
# create a program using maths and f-strings that tells us how many days, weeks or months we have left to live
# until 90 Years old.
# It will take your current age as the input and output a message with our time left in this format
# You have x days, y weeks and z months left.

# where x, y and z are replaced with the actual calculated numbers.
# Warning: your output should match the example output format exactly, even the positions of the commas and full stops.

# we have
# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

# Dont change the code below
age = input("what is your current age? ")
days = (90 * 365) - (int(age) * 365)
weeks = (90 * 52) - (int(age) * 52)
months = (90 * 12) - (int(age) * 12)

# Write your code below
years_left = (f"You have {days} days, {weeks} weeks, and {months} months left.")
print(years_left)