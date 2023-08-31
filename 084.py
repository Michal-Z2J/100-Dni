'''
Napisz program, który oblicza pole powierzchni koła i wypisuje wynik z zaokrągleniem 
do dwóch miejsc po przecinku. Użyj f-stringów do formatowania wydruku.

1. Poproś użytkownika o podanie promienia koła (r) jako liczby zmiennoprzecinkowej.
2. Oblicz pole powierzchni koła za pomocą wzoru: pole = π * r^2 (możesz użyć wartości pi z modułu math).
3. Wypisz wynik zaokrąglony do dwóch miejsc po przecinku, używając f-stringów.
'''
import math

while True:
    try:    
        r = float(input("Podaj promień koła ('exit' aby zamknąć program): "))
        pole = math.pi * r**2
        print(f"Pole koła o promienu {r} wynosi: {pole:.2f}")
    except Exception as error:
        if str(error) == "could not convert string to float: 'exit'":
            print("Zakończono działanie programu. ")
            break
        else:
            print("Wprowadzone dane nie są liczbą o odpowiednim formacie. Spróbuj jeszcze raz.")

