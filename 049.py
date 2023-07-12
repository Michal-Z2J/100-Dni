# This Python file uses the following encoding: Windows-1250
import os, sys

"""
Stwórz program, który będzie przechowywał słownik z nazwami państw i ich stolicami. 
Następnie poproś użytkownika o podanie nazwy państwa, a program ma wyświetlić stolicę tego państwa. 
Jeśli użytkownik poda nazwę państwa, której nie ma w słowniku, program powinien wyświetlić komunikat o błędzie.
"""

countries = {
    'Albania': 'Tirana',
    'Andora': 'Andora',
    'Austria': 'Wiedeń',
    'Belgia': 'Bruksela',
    'Białoruś': 'Mińsk',
    'Bośnia i Hercegowina': 'Sarajewo',
    'Bułgaria': 'Sofia',
    'Chorwacja': 'Zagrzeb',
    'Czarnogóra': 'Podgorica',
    'Czechy': 'Praga',
    'Dania': 'Kopenhaga',
    'Estonia': 'Tallinn',
    'Finlandia': 'Helsinki',
    'Francja': 'Paryż',
    'Grecja': 'Ateny',
    'Hiszpania': 'Madryt',
    'Holandia': 'Amsterdam',
    'Irlandia': 'Dublin',
    'Islandia': 'Reykjavik',
    'Kazachstan': 'Astana',
    'Kosowo': 'Prisztina',
    'Liechtenstein': 'Vaduz',
    'Litwa': 'Wilno',
    'Luksemburg': 'Luksemburg',
    'Łotwa': 'Ryga',
    'Macedonia Północna': 'Skopje',
    'Malta': 'Valletta',
    'Mołdawia': 'Kiszyniów',
    'Monako': 'Monako',    
    'Niemcy': 'Berlin',
    'Norwegia': 'Oslo',
    'Polska': 'Warszawa',
    'Portugalia': 'Lizbona',
    'Rosja': 'Moskwa',
    'Rumunia': 'Bukareszt',
    'San Marino': 'San Marino',
    'Serbia': 'Belgrad',
    'Słowacja': 'Bratysława',
    'Słowenia': 'Lublana',
    'Szwajcaria': 'Berno',
    'Szwecja': 'Sztokholm',
    'Turcja': 'Ankara',
    'Ukraina': 'Kijów',
    'Węgry': 'Budapeszt',
    'Wielka Brytania': 'Londyn',
    'Włochy': 'Rzym'
}

def get_country():
    country = input("Podaj nazwę państwa: ")
    return country

user_country = get_country()
if user_country in  countries:
    print("Państwo: ", user_country, ", Stolica: ", countries[user_country])
else:
    print("Błąd. Podana nazwa państwa nie istnieje lub nie znajduje się w słowniku.")
