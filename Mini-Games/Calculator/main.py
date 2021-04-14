from art import logo
print(logo)


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide}

def calculator():
    num1 = float(input("What's the first number?: "))
    
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    
    num2 = float(input("What's the second number?: "))
    
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    again = input("Type 'y' to continue calculating with {answer}, or type 'n' to exit or type 'r' to restart: ")
    if again == "y":
        should_continue = False
    elif again == "n":
        should_continue = True
    elif again == "r":
        should_continue = True
        calculator()
    
    while not should_continue:
        old_answer = answer
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick another operation: ")
        num3 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(answer,num3)
        print(f"{old_answer} {operation_symbol} {num3} = {answer}")
        again = input("Type 'y' to continue calculating with {answer}, or type 'n' to exit or type 'r' to restart: ")
        if again == "n":
            should_continue = True
        elif again == 'r':
            should_continue = True
            calculator()

calculator()
