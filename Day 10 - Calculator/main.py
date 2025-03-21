import art
#Functions for what to do with each operation
def add(n1, n2):
    """Function to add 2 numbers (n1 and n2) together"""
    return n1 + n2
def sub(n1, n2):
    """Function for subtraction of n1 by n2"""
    return  n1 - n2
def mult(n1, n2):
    """Function to multiply n1 by n2"""
    return n1 * n2
def div(n1, n2):
    """Function to divide n1 by n2"""
    return n1 / n2
#Dictionary to store the above created functions
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}

def get_user_input(n1=""):
    """Function to get input from the user before the calculations take place"""
    if not n1:
        n1 = (input("Please Enter the first number you'd like to calculate with\n"))
    operation = input("Please enter the operation you'd like to use\n '+'\n'-'\n'*'\n'/'\n")
    n2 = (input("Please enter the second number for this calculation\n"))
    return n1, operation, n2

def after_calculation_input():
    """Function to get input from the user for if they want to keep using the program and keep the previous result"""
    keep_memory = input("Would you like to keep working with result from this calculation? 'y' or 'n'\n")
    if keep_memory == 'y':
        keep_memory = True
        #assume that if the user wants to keep the memory they want to keep using the program so we can skip asking to quit
        leave = False
        return keep_memory, leave
    else:
        keep_memory = False
    leave = input("Would you like to exit the program 'y' or 'n'\n")
    if leave == 'y':
        leave = True
    else:
        leave = False
    return keep_memory, leave

def input_validation(n1, operation, n2):
    """Function to take initial user inputs and validate if they will cause any errors and get the user to correct if they won't work"""
    possible_operations = "+-*/"
    #Check if n1 is a number or not
    n1_check = False
    while not n1_check:
        try:
            float(n1)
        except ValueError:
            n1 = input("Please enter a valid number for the first part of your calculation")
        else:
            n1_check = True

    #Check if the operation selected is one supported by this program
    operation_check = False
    while not operation_check:
        if operation not in possible_operations:
            operation = input("Please enter a valid operation\n '+'\n '-'\n '*'\n '/'\n")
        else:
            operation_check = True

    #Check if n2 is a valid number or not
    n2_check = False
    while not n2_check:
        try:
            float(n2)
        except ValueError:
            n2 = input("Please enter a valid number for the second part of your calculation")
        else:
            n2_check = True

    #Check to ensure the user isn't trying to divide by zero
    while operation == "divide" and n2 == 0:
        n2 = input("Please don't try and divide by 0, please enter a new number to divide by")
    #return either the initial or corrected values
    return n1, operation, n2

def program(n1, operation, n2):
    """Function to perform the requested calculation and get the post calculation output"""
    n1, operation, n2 = input_validation(n1, operation, n2)
    result = operations[operation](float(n1), float(n2))
    print(f"{n1} {operation} {n2} = {result}")
    keep_memory, leave = after_calculation_input()
    return result, keep_memory, leave

#Run the program until the user exits
leave = False
print(art.logo)
while not leave:
    n1, operation, n2 = get_user_input()
    result, keep_memory, leave = program(n1, operation, n2)
    while keep_memory and not leave:
        n1, operation, n2 = get_user_input(result)
        result, keep_memory, leave = program(n1, operation, n2)



