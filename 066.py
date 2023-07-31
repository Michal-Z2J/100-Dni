'''
Napisz program, który odczyta plik tekstowy zawierający listę tych produktów. 
Następnie program powinien wyświetlić na ekranie nazwy produktów, 
których cena jest mniejsza niż 8 złotych.
'''

file_path = "066.txt"
f = open(file_path, "r", encoding="utf-8")
list_from_file = f.read().splitlines()
f.close()

products_list = []
for i in list_from_file:
    products_list.append(i.split(","))

for x in products_list:
    if float(x[1]) < 8:
        print(f'{x[0]:6} - {x[1]}')

#-----Używając słownika-----
print("-------------")
products_dict = {}
for j in list_from_file:
    nazwa, cena = j.split(",")
    products_dict[nazwa] = float(cena)
    if float(cena) < 8:
        print(f'{nazwa:6} - {cena}')