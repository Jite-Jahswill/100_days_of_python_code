# coding challenge 1
# Funtions with output

def format_name(f_name, l_name):
    new_f_name = f_name.title()
    new_l_name = l_name.title()
    return f"{new_f_name} {new_l_name}"
    

f_name = print(input("Tell us your First name ")).lower()
l_name = print(input("Tell us your Last name ")).lower()


new_name = format_name(f_name=f_name, l_name=l_name)

print(new_name)

# Coding challenge 2
# Instructions 

# In the starting code,  youll find the solution from the leap year challenge. First, convert this function is_leap()
# so that instead of printing leap year or not leap year. it should return True if it is leap year and return false if it is not
# a leap year.
# You are going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
# days in a month(year = 2022, month = 2)
# 
# And it will use this information to work out the number of days in the month, and then return that as the output, e.g;
# 28
# the list month_days contains the number of days in a month from jan to dec for a leap year. A leap year has 29 days in february.

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]
    
# Do Not change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)