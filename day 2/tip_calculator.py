# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person shoul pay (150.00 / 5) * 1.12
# round the numbers to two decimal place

# bill = input("what is your bill? ")
# Percentage = 100 * float(bill)/float(whole)
# final = str(Percentage)

bill = float(input("What is your bill? "))  # prompt user to enter bill amount and convert to float
num_people = int(input("How many people would you like to split the bill with? "))  # prompt user to enter number of people and convert to integer
tip_percent = float(input("What percentage of tip do you want to pay? "))  # prompt user to enter tip percentage and convert to float

tip_amount = bill * (tip_percent / 100)
total_amount = bill + tip_amount
amount_per_person = total_amount / num_people

print(f"Each person should pay ${amount_per_person:.2f}")  # print the amount per person with two decimal places


# OR
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${final_amount}")