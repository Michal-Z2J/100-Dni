import os, sys
"""
1. Dopisz operacje: potęgowania, wyznaczania reszty z dzielenia
2. Dodaj możliwość przeliczania jednostek miar (długości i ciężaru).
"""

def perform_calculation(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "One does not simply divide by zero!"
        else:
            return num1 / num2
    elif operator == "**":
        return num1**num2
    elif operator == "%":
        return num1 % num2
    else:
        return "Invalid operator"

def get_number(prompt):
    while True:
        num_str = input(prompt)
        if num_str == "exit":
            return num_str
        if num_str.isdigit() or (num_str.startswith("-") and num_str[1:].isdigit()):
            return float(num_str)
        print("Invalid input. Please enter a number.")

def get_operator():
    while True:
        operator = input("Enter operator (+,-,*,/,**,%): ")
        if operator in ["+", "-", "*", "/", "**", "%"]:
            return operator
        if operator == "exit":
            return operator
        print("Invalid operator. Please enter +, -, *, /, ** or %.")

def print_result(num1, num2, operator, result):
    print("Result:", result)
    input("Press Enter to continue...")
    os.system("cls" if os.name == "nt" else "clear")

def run_calculator():
    num1 = get_number("Enter first number: ")
    if num1 == "exit":
        return False
    num2 = get_number("Enter second number: ")
    if num2 == "exit":
        return False
    operator = get_operator()
    if operator == "exit":
        return False
    result = perform_calculation(num1, num2, operator)
    print_result(num1, num2, operator, result)
    return True

def desc():
    print("Welcome to the calculator.")
    print("Calculator supports addition, subtraction, multiplication, division, exponentiation and finding the remainder of the division.")
    print("To exit, type 'exit'.")
    print()

ok = True
while ok:
    desc()
    ok = run_calculator()
