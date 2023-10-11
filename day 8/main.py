############ Functions with inputs ###########

# coding challenge 1
# we can pass values to functions
# def my_function(something):
#     do something

# here we see that we can pass something into our function and it can do something. e.g. numbers or other data

# function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do? {name}")
    print("Isn't the weather nice today?")
    
    
greet_with_name("Angela")

# this function changes with input. Parameter is the name inside the function and the argument is the value of the data

# Multiple
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How do you do? {name}")
    print("Isn't the weather nice today?")
    print(f"Hows the weather in {location}")
    
greet_with("Jack Bauer", "Nowhere")

# when we swich the order it becomes complete nonsense because name goes to location and verse versal
# to stop this we can do (a=1, b=2, c=3)

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How do you do? {name}")
    print("Isn't the weather nice today?")
    print(f"Hows the weather in {location}")
    
greet_with(name="Jack Bauer", location="Nowhere")

# Coding Challenge 2
# coding challenge 3

#Simple Function
def greet():
  print("Hello Angela")
  print("How do you do Jack Bauer?")
  print("Isn't the weather nice today?")
greet()

#Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greet_with_name("Jack Bauer")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#Calling greet_with() with Positional Arguments
greet_with("Jack Bauer", "Nowhere")
#vs.
greet_with("Nowhere", "Jack Bauer")


#Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Angela")