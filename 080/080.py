'''
Twoim zadaniem jest napisanie prostego skracacza adresów URL, który będzie umożliwiał 
skracanie długich adresów internetowych do krótszych, łatwiejszych do zapamiętania wersji. 
Program powinien zapisywać skrócone (oraz pełne) adresy do pliku, a następnie odczytywać je przy kolejnym uruchomieniu.

Wymagania:
Napisz program, który wczytuje adres URL od użytkownika.
Program powinien generować unikalny krótki identyfikator dla każdego adresu URL.
Pary adresów powinny być zapisywane w pliku w formacie tekstowym
Przy uruchomieniu programu, wczytaj zapisane wcześniej adresy z pliku.
Użytkownik powinien mieć możliwość wprowadzenia skróconego adresu, aby uzyskać pierwotny, długi adres URL.

Sugestie:
Użyj funkcji skrótu (np. hashlib w Pythonie) do generowania unikalnych identyfikatorów dla adresów URL.
Zastanów się nad zastosowaniem algorytmu Base62 do konwersji identyfikatorów na krótsze ciągi znaków.
Aby sprawdzić, czy dany skrócony adres URL istnieje, użyj struktury danych, takiej jak słownik (dictionary) w Pythonie.
'''

import os
import hashlib
import base64

def get_ID(url):
    return hashlib.md5(bytes(url, 'utf-8')).hexdigest()

def shorten_ID(hash):
    result = base64.b64encode(bytes(hash, 'utf-8')[:10])
    return result.decode().strip('=')

def read_file(file_path):
    temp_dict = {}
    if os.path.exists(file_path) == False:
        return temp_dict
    else:
        with open(file_path, "rt") as file:
            for line in file:
                ID_url, url = line.strip().split("\t")
                temp_dict[ID_url] = url
    return temp_dict

def add_to_file(file_path, ID_short, user_url):
    with open(file_path, "at") as file:
        file.write(f"{str(ID_short)}\t{str(user_url)}\n")

def desc():
    print("Witaj w programie do skracania adresów URL.")
    print("Wprowadzony adres URL zatwierdź przy użyciu 'Enter'.")
    print("Aby uzyskać pierwotny adres URL z bazy danych, należy podać jego skrót poprzedzając go znakiem '#', np. '#jakiś_skrót'")
    print("Aby zakończyć program naciśnij 'Enter' bez wprowadzania żadnych danych.")
    print("")

file_path = "080_url_database.txt"
url_dict = {}
desc()

while True:
    url_dict = {}
    user_url = str(input("Podaj adres URL do skrócenia lub uzyskania oryginalnego adresu URL (#): "))
    if user_url == "":
        print("Zakończono działanie programu.")
        break
    if user_url[0] == "#":        
        url_dict = read_file(file_path)
        if user_url[1:] in url_dict:
            print(url_dict[user_url[1:]])
        else:
            print("Brak adresu url dla podanego skrótu, spróbuj ponownie.")
    else:        
        url_dict = read_file(file_path)
        
        if user_url in url_dict.values():
            print("Podany adres url znajduje się już w bazie danych.")
        else:
            ID_hash = get_ID(user_url)
            ID_short = shorten_ID(ID_hash)
            add_to_file(file_path, ID_short, user_url)
            url_dict = read_file(file_path)