'''
Napisz kod, który będzie prosił o dwie liczby i będzie je dzielił. 
Zadbaj przy pomocy try / except, o blokadę dzielenia przez 0.
'''

def calculation(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        return "Error! One does not simply divide by zero!"

while True:
    try:
        firstNumber = input("Podaj pierwszą liczbę: ")
        firstNumber = float(firstNumber)
        secondNumber = input("Podaj drugą liczbę: ")
        secondNumber = float(secondNumber)
        result = calculation(firstNumber, secondNumber)
        print("Wynik: ", result)
    except ValueError:
        print("Zakończono działanie programu.")
        break