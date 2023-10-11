# Coding Challenge 1
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
import math

def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
    
greet()


# Coding Challenge 2
# Instructions 


# Write your code here
def print_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} to paint the wall.")


# Dont touch this code
test_h= int(input("Height of wall: "))
test_w= int(input("width of wall: "))
coverage = 5
print_calc(height=test_h, width=test_w, cover=coverage)

# coding challenge 3
# Prime number checker
# Prime numbers are numbers that can only be divided by 1 and itself.

def prime_checker(number):
    for i in range(2, number):
        is_prime = True
        if number % i == 0:
           is_prime = False
    if is_prime:
         print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
        
        
n = int(input("Check this number: "))
prime_checker(number=n)