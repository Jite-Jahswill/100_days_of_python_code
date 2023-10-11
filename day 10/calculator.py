# START
# from art import logo

def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# create a dictionary with keys as operators and values as function name

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    # print(logo)
    
    num1 = float(input("Whats the first number?: "))
    # operation["+"]= add
    # operation["-"]= subtract
    # operation["*"]= multiply
    # operation["/"]= divide

    for symbol in operation:
        print(symbol)

    calc_end = True

    while calc_end:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("Whats the next number?: "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        option = input("Type 'y' to continue the operation or type 'n' to start a new calculation.: ").lower()
        if option == "y":
            num1 = answer
        else:
            calc_end = False
            calculator()

    # if operation_symbol == "+":
    #     add(num1, num2)
    # if operation_symbol == "-":
    #     subtract(num1, num2)
    # if operation_symbol == "*":
    #     multiply(num1, num2)
    # if operation_symbol == "/":
    #     divide(num1, num2)

calculator()

# here if the user types no we rerun the calculation i.e. reset else we continue calculation
# do not call calculator inside the while loop it would loop except theres a condition.