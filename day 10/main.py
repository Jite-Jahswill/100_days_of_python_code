############# Functions with Output ##############

# last time we learnt how to define functions uding def and collects something def my_function(something) known 
# Functions with input.

# what about funtion with output 
def my_function():
    result = 3 * 2
    return result

output = my_function()

# now the value of result is returned and can be saved anywhere above output = 6 (3*2)
# Functions can be liking to a processing factory machine they process a grounp of inputs

# Coding Challenge 1

# More than one return statement
def format_name(f_name, l_name):
    if f_name== "" or l_name == "":
        return "You didnt provide valid inputs. "
    new_f_name = f_name.title()
    new_l_name = l_name.title()
    return f"{new_f_name} {new_l_name}"

# here if we have an empty name it returns a message

# Coding Challenge 2

# Docstrings
# Docstrings help us make documents while coding
# docstrings are documents that are shown when we hover on functions e.g. len().
# """write ur doc in between"""

def format_name(f_name, l_name):
    
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name== "" or l_name == "":
        return "You didnt provide valid inputs. "
    new_f_name = f_name.title()
    new_l_name = l_name.title()
    return f"{new_f_name} {new_l_name}"

format_name()
# now we have docs for our above function
# we can use """""" for muli line comment

# Calculator

# difference between print and return
# return function helps us tore data that can be reused.
