'''
Napisz program, który losuje 5 liczb całkowitych z zakresu od 1 do 10, 
a następnie prosi użytkownika o odgadnięcie co najmniej jednej z tych liczb. 
Program powinien odpowiedzieć, czy podana przez użytkownika liczba była jedną z wylosowanych lub nie.

'''
import random
print("Wylosowaliśmy 5 liczb z zakresu od 1 do 10. Spróbuj zgadnąć jedną z nich.")
print("Wpisz liczbę od 1 do 10 i naciśnij 'Enter', aby zatwierdzić wybór.")
print("Naciśnij 'Enter' bez wpisywania żadnego znaku, aby zakończyć działanie programu.")

while True:
    try:
        numbers = random.sample(range(1, 11), k=5)
        answer = input("Twoja odpowiedź to: ")
        if int(answer) in numbers:
            print("Gratulacje, trafiłeś! Wylosowane liczby to: ", numbers)
        elif int(answer) < 1:
            print("Podana liczba jest za niska. Wylosowane liczby są w przedziale od 1 do 10.")
        elif int(answer) > 10:
            print("Podana liczba jest za wysoka. Wylosowane liczby są w przedziale od 1 do 10.")
        else:
            print("Spróbuj jeszcze raz.")
    except ValueError:
        if answer == "":
            break
        else:
            print("Error! Program przyjmuje tylko liczby od 1 do 10. Spróbuj jeszcze raz wpisując poprawne dane.")