'''
Napisz funkcję divide(a, b), która dzieli dwie liczby. 
Funkcja powinna zgłaszać wyjątki w następujących sytuacjach:

Jeśli a lub b nie są liczbami, zgłoś TypeError.
Jeśli b wynosi 0, zgłoś ZeroDivisionError.
Jeśli a lub b są ujemne, zgłoś własny wyjątek NegativeNumberException.
Następnie użyj bloku try...except, aby przechwycić i obsłuży każdy z tych wyjątków indywidualnie.
'''
class NegativeNumberException(Exception):
    pass

def divide(a, b):
    if a < 0 or b < 0:
        raise NegativeNumberException("Wprowadzone liczby nie mogą być ujemne. Spróbuj jeszcze raz.")
    print(f"Wynik dzielenia liczby {a} i {b} wynosi: {a/b:.3f}")
    
while True:
    try:
        num1 = float(input("Podaj pierwszę liczbę (exit aby zakończyć program): "))
        num2 = float(input("Podaj drugą liczbę (exit aby zakończyć program): ")  ) 
        divide(num1, num2)
    except TypeError as type_err:
        print("Wprowadzone liczby muszę być liczbami. Spróbuj jeszcze raz.")
        print(f"Błąd: {type_err}")
    except ZeroDivisionError as zero_err:
        print("Nie można dzielić przez zero. Spróbuj jeszcze raz.")
        print(f"Błąd: {zero_err}")    
    except NegativeNumberException as neg_err:
        print(f"Błąd: {neg_err}")
    except ValueError as val_err:
        if str(val_err) == "could not convert string to float: 'exit'":
            print("Zakończono działanie programu")
            break
        else:
            print("Wprowadzone liczby muszę być liczbami. Spróbuj jeszcze raz.")
            print(f"Błąd: {val_err}")