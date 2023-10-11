########### DICTIONARY AND NESTING ###########

# dictionaries in pytho works the same as dictionaries we have key and value {key: value} objects in JS
# {"Bug": "An error in a program that prevents the program from running as expected.",
# "Function": "A piece of code that you can esily call over and over again.",
# "Loop": "The action of doing something over and over again."}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can esily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# to call the item from the dictionary just say
print(programming_dictionary["Bug"])
# if we put in a key that doesnt exist we get an error
# without the strings we get an error mession because it would be considered a variable. numbers can be represented 
# without strings.
# 
# Adding new items to dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again."
# creates a new item to d dictionary
# we can also create empty dictionaries and add to it using the example above

empty_dictionary = {}
# empty_dictionary[] = ""
empty_dictionary["Food"] = "what we eat to survive"

# to wipe an existing dictionary do
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key) # only keys are printed out
    print(programming_dictionary[key]) # now we get the value
    
# Coding challenge 1


########### NESTING ############
# { key: [list], key2: {dict}}
# up there we try to store complex data

# Simple dictionary
capitals = {
    "France": "paris",
    "Germany": "Berlin",
}

# Nested list in dic
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting dictionaries in dictionaries
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 31},
}

# nesting dictionaries in a list
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12},
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 31},
]

# Coding Challenge 3