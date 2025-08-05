def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation in operations:
    result = operations[operation](first_number, second_number)
    print(f"The result of {first_number} {operation} {second_number} is {result}")
else:
    print("Invalid operation.")
