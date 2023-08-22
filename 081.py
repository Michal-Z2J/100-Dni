'''
Napisz funkcję o nazwie compare_numbers(), która przyjmuje dwie liczby zmiennoprzecinkowe 
jako argumenty i porównuje je, uwzględniając potencjalne błędy zaokrąglenia. 
Funkcja powinna zwracać True, jeśli liczby są równe (z tolerancją błędu 1e-9), i False w przeciwnym razie.
'''

def compare_numbers(x, y):
    if abs(x-y) < 1e-9:
        return True
    else:
        return False

print("Witaj w programie do porównywania dwóch liczb.")
print("Wprowadzanie liczb zatwierdź przez naciśnięcie klawisza 'Enter'.")
print("Aby zakończyć działanie programu naciśnij 'Enter' bez wprawadzania żadnych danych.")

while True:
    try:
        a = float(input("Podaj pierwszą liczbę do porównania: "))
        b = float(input("Podaj drugą liczbę do porównania: "))
        result = compare_numbers(a, b)
        print(result)

    except Exception as error:
        if str(error) == "could not convert string to float: ''":
            print("Zakończono działanie programu.")
            break
        else:
            print("Błąd programu:", error)