'''
Stwórz plik todo.txt. 
Następnie napisz program, który pobierze od użytkownika listę zadań do zrobienia 
(np. zakupy, sprzątanie, pranie itp.) i zapisze je do tego pliku 
(rozszerzając ten plik o nowe zadania, bez kasowania starych).
'''
import os

def read_file(file_path):
    f = open(file_path, "r")
    list = f.read().splitlines()
    print("Twoja lista zadań: ")
    if os.stat(file_path).st_size == 0:
        print("Lista jest pusta.")
    else:
        for i in list:
            print("- ", i)
    f.close()
    print("")

def add_task(file_path):
    f = open(file_path, "a")
    task = " "
    while True:    
        task = input("Dodaj zadanie do listy: : ")
        if task == "":
            f.close()
            print("")
            break
        else:
            f.write(task + '\n')

def read_new_file(file_path):
    f = open(file_path, "r")
    list = f.read().splitlines()
    print("Twoja aktualna lista zadań: ")
    if os.stat(file_path).st_size == 0:
        print("Lista jest pusta.")
    else:
        for i in list:
            print("- ", i)
    f.close()
    print("")

print("Witaj w programie do tworzenia listy zadań - TODO.")
print("Wprowadzone zadanie zatwierdź przy użyciu 'Enter'.")
print("Aby zakończyć wpisywanie zadań naciśnij 'Enter' bez wprowadzania żadnych danych.")
print("")

file_path = "todo.txt"
read_file(file_path)
add_task(file_path)
read_new_file(file_path)