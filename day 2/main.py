# Data Types

# strings = "Hello"
print("hello"[0])
# 0 here indicates the first character and 4 indicates the last character
# "123"+"345" would no be calculated but we get 123345

# Integer (Numbers without decimal places)
print(123+345)
# 468 because its being calculated
# Large Integers are seperated using underscore 342,654,896 would be 342_654_896 the computer ignores the _

# challenge 1

# Float (Numbers with decimal places)
# 3.14159 numbers of pi (floating point number)

# Boolen (test for true or false in a program)
True
False

# functions are machines that process products and wrong products gives error
# to convert numbers to string we do

num_char = len(input("what is your name?"))

new_num_char = str(num_char)

print("Your name has" + new_num_char + "characters.")
a = str(123)
print(type(a))
# challenge 2

print(70 + float("100.5"))# we get 170.5 numbers
print(str(70)+str(100))# we get 70100 strings

# Substraction multiplication and division
# PEMDAS (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction) LR (Left to right)
# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3
# 2 ** 2(2 to the power of 2)

# Modification of numbers

# to round numbers do
print(round(8/3)) # we get 3

# Also we can specify the number of places after the decimal point
print(round(8/3, 2)) # we get 2.67

# we can covert to int doing
print(8 // 3) # we get 2 and a type of int

results = 0

results += 3 # same as -= /= *=

# to mixed all data type to string do
score = 0
height = 1.8
isWinning = True

#f-String
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}") 
# all don without manual 
# conversion like int() str() float() boolean() 
# challenge 3