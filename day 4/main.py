########### Randomisation and Python Lists #############

import random
import my_module
# our module file is imported

random_integer = random.randint(1, 10)
print(random_integer)

# here we get a random whole number between 1 and 10

# Module are splitted codes that function for one thing like building a car where different people work
# random is an example of a module. It was created to ease random number calculations.

print(my_module.pi)
# here we get the value of pi from my_module.pi

# create a random floating poin number
random_float = random.random()
print(random_float)
# this generates a number between 0 and 1 but never 1

# to get random floating numbers between 0 and 5
randomFLoat = random.random() * 5
print(randomFLoat)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# Coding challenge 1

########## Lists ###########

# we can store connected data using list instead of using state= alabama, state= houston. nope but we use list(array in JS)
# fruits = [item1, item2]
# fruits = ["cherry", "apple", "pear"]
states_of_america = ["Delaware", "Pennsylvania"]

print(states_of_america[0])
# Delaware is printed because 0 is the first because of 0's and 1's
print(states_of_america[-1])
# -1 is the last item in the list

# we can alson change items
states_of_america[1] = "pencilvania"

# to push do
new_state = states_of_america.append('Angelaland')

# To extend meaning to extend the list by appending all items from the iterable.
states_of_america.extend(["angelaland","jack bauer land"])

# we have .insert(i,x) to insert at a particular position, .remove(X), .pop([i]) removes one but .pop() removes all, .clear()
# coding Challenge 2


###### nested lists ########

# if we try to access a list that is not there you get an off by 1 error. or list index out of range if you do len(names) always minus
# 1 to cover for zero

# using high pesticide food for our list say
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches",
               "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# here we have fruits and vegetables together we can seperate using

fruits = ["strawberries", "Nectarines", "Apples", "Grapes", "Peaches",
               "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# or do

dirty_dozen = [fruits, vegetables]
# we now have a list that contains two list [["spinach"]["strawberries"]]
# Coding Challenge 3