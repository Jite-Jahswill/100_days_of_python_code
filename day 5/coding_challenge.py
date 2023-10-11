# coding challenge 1

# Instructions
# You are going to write a program that calculates the average students height from a list of heights.
# e.g. students_heights = [180, 124, 165, 173, 189, 169, 146]
# 
# The average height can be calculated by adding all the heights together and dividing by the total number of
# heights.
# e.g.
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights
# 1146 ÷ 7 = 163.71428571428572
# Average height rounded to the nearest whole number = 164

# Dont touch this code
student_height = input("Input a list of student height").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

# write your code here
total_height = sum(student_height)
number_of_students = len(student_height)
average_height = round(total_height / number_of_students)
print(average_height)

# using for loops
total_height = 0
for height in student_height:
    total_height += height

number_of_students = 0
for student in student_height:
    number_of_students += 1
    
average_height = round(total_height / number_of_students)
print(average_height)


# Coding Challenge 2
# Instructions 
# You are going to write a program that calculates the height score from a list of scores
# e.g. student_score = [78, 65, 89, 86, 55, 91, 64, 89]
# important you are not allowed to use the max or min functions. The output words must match the exsmple i.e
# The highest score in the class is: x
# 
# Dont touch this code
student_scores = input("Input a list of students score ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# Write your code below
print(max(student_scores))
print(min(student_scores))
# using max()
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
        
lowest_score = 0
for score in student_scores:
    if score < lowest_score:
        lowest_score = score
        
        
        
# Coding Challenge 3
# Instruction 
# You are going to write a program that calculates the sum of all even numbers from 1 to 100,
# including 1 and 100.
# 
# e.g. 2 + 4 + 6 + 8 + 10 ... + 98 + 100
# 
# Important, there should only be 1 print statement this problem, but you will need to use the range() function
# in any of the solutions.
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

# or
total2 = 0
for number in range(1, 101):
    if number % 2 == 0: 
        total2 += number
print(total2)



# Coding Challenge 4
# Instructions 
# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# 
# Your program should print each number from 1 to 100 in turn
# when the number is divisible by 3 then instead of printing the number it shoulf print "Fizz".
# When the number is divisible by 5 it should print "Buzz" instead of the number.
# And when the number is divicible by 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# 
# Write your code below
for number in range(1, 101):
    if number % 3 and number % 5 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("FizzBuzz")
    else:
        print(number)