# This Python file uses the following encoding: Windows-1250
import os, sys
"""
Masz napisać kalkulator :)
Poproś użytkownika o dwie liczby (najpierw jedną, potem drugą)
Poproś użytkownika o działanie, jakie ma być wykonane (+,-,/,*)
Wyświetl rezultat działania na ekranie :)
Wróć na początek.
Wpisanie exit powinno zakończyć działanie kalkulatora.
"""

def calculation(number1, number2, char):
    if char == "+":
        return number1 + number2
    elif char == "-":
        return number1 - number2
    elif char == "*":
        return number1 * number2
    elif char == "/":
        return number1 / number2

while True:
    firstNumber = input("Podaj pierwszą liczbę: ")
    secondNumber = input("Podaj drugą liczbę: ")
    operation = input("Podaj działanie jakie ma zostać wykonane: ")
    result = calculation(firstNumber, secondNumber, operation)
    print("Wynik: ", result)
    ending = input(
        'Zakończ program wpisując "exit", aby kontynuować naciśnij "Enter": '
    )
    if ending == "exit":
        break
