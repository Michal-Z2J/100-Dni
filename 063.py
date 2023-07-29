'''
Napisz kod, który będzie prosił o dwie liczby i będzie je dzielił. 
Zadbaj przy pomocy try / except, o blokadę dzielenia przez 0.
'''

def calculation(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        return "Error! One does not simply divide by zero!"
    
print("Witaj w programie do dzielenia dwóch liczb.")
print("Wprowadzanie liczb zatwierdź przez naciśnięcie klawisza 'Enter'.")
print("Aby zakończyć działanie programu naciśnij 'Enter' bez wprawadzania żadnych danych.")

while True:
    try:        
        firstNumber = input("Podaj pierwszą liczbę: ")
        firstNumber = float(firstNumber)
        secondNumber = input("Podaj drugą liczbę: ")
        secondNumber = float(secondNumber)
        result = calculation(firstNumber, secondNumber)
        print("Wynik:", result)
    except Exception as error:
        if str(error) == "could not convert string to float: ''":
            print("Zakończono działanie programu.")
            break
        else:
            print("Błąd programu:", error)        