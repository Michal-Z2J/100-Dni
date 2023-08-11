'''
Pamiętasz kalkulator? Na pewno :) Dodaj do niego docstringową dokumentację :)
'''
import os

def perform_calculation(num1, num2, operator):
    """
    Wykonuje operacje dodawania, odejmowania, mnożenia, dzielenia, potęgowania
    i znajdowania reszty z dzielenia dwóch liczb. Po wykonaniu obliczeń zwraca wynik.
    Dodatkowo zapobiega dzieleniu przez zero i wprowadzania złego znaku.

    Argumenty:
    num1 -- pierwsza liczba
    num2 -- druga liczba
    operator - znak operacji jaka ma być wykonana

    Zwraca:
    Wynik podanej operacji na liczbach num1 i num2.
    """
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
    """
    Funkcja odczytuje input wprowadzony przez użytkownika i sprawdza
    czy jest liczbą bądź napisem 'exit'.
    W przeciwnym wypadku funkcja prosi ponowne wprowadzenie danych.

    Argumenty:
    prompt -- input użytkownika
    
    Zwraca:
    Liczbę podaną przez użytkownika jako float albo napis 'exit'.
    """
    while True:
        num_str = input(prompt)
        if num_str == "exit":
            return num_str
        if num_str.isdigit() or (num_str.startswith("-") and num_str[1:].isdigit()):
            return float(num_str)
        print("Invalid input. Please enter a number.")

def get_operator():
    """
    Funkcja pobiera input wprowadzony przez użytkownika i sprawdza
    czy jest odpowiednim znakiem (+,-,*,/,**,%) bądź napisem 'exit'.
    W przeciwnym wypadku funkcja prosi ponowne wprowadzenie danych.

    Argumenty:
    brak
    
    Zwraca:
    Znak operacji podany przez użytkownika albo napis 'exit'.
    """
    while True:
        operator = input("Enter operator (+,-,*,/,**,%): ")
        if operator in ["+", "-", "*", "/", "**", "%"]:
            return operator
        if operator == "exit":
            return operator
        print("Invalid operator. Please enter +, -, *, /, ** or %.")

def print_result(result):
    """
    Funkcja wyświetla wynik wcześniej przeprowadzonej operacji matematycznej.
    Następnie czyści ekran po naciśnięciu 'Enter' przez użytkownika.

    Argumenty:    
    result -- wynik działania

    Zwraca:
    brak
    """
    print("Result:", result)
    input("Press Enter to continue...")
    os.system("cls" if os.name == "nt" else "clear")

def run_calculator():
    """
    Funkcja pobiera input od użytkownika i przekazuje do funkcji 'get_number' i 'get_operator',
    jednocześnie sprawdzając czy nie jest on napisem 'exit'.
    Nastepnie przekazuje dane o liczbach i znaku operacji do funkcji 'perform_calculation'.
    Na koniec przekazuje wynik operacji do funkcji 'print_result'.

    Argumenty:
    brak

    Zwraca:
    Zwraca 'True' w przypadku prawidłowego wykonania operacji i wyświetlenia wyniku, bądź 'False' jeżeli input to napis 'exit'.
    """
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
    print_result(result)
    return True

def desc():
    """
    Wyświetla na ekranie tekst z opisem i wyjaśnieniem działania programu.

    Argumenty:
    brak

    Zwraca:
    brak
    """
    print("Welcome to the calculator.")
    print("Calculator supports addition, subtraction, multiplication, division, exponentiation and finding the remainder of the division.")
    print("To exit, type 'exit'.")
    print()

ok = True
while ok:
    desc()
    help(run_calculator)
    ok = run_calculator()
