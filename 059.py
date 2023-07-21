'''
Napisz funkcję, która przyjmuje listę liczb całkowitych i zwraca listę 
zawierającą tylko unikalne wartości z tej listy.
'''

user_input = " "
user_list = []
print("Wprowadź dowolną ilość liczb całkowitych.")
print("Wybór liczby zatwierdź przy użyciu 'Enter'.")
print("Aby zakończyć wprowadzanie liczb naciśnij 'Enter'.")

while user_input != "":
    user_input = input()
    if user_input.isdigit() is True:
        user_list.append(user_input)
    elif user_input.startswith("-"):
        user_list.append(user_input)
    else:
        if user_input == "":
            break
        else:
            print("Wprowadzona wartość nie jest liczbą całkowitą. Wprowadź liczbę jeszcze raz.")

no_duplicates = set(user_list)

for i in no_duplicates:
    print(i, end=" ")