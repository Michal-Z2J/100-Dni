'''
Przygotuj prosty słownik (dosłownie) polsko - angielski. 10-20 wyrazów max.
Następnie komputer ma poprosić o wpisanie przez Ciebie zdania. 
Po jego wprowadzeniu ma przetłumaczyć wszystkie wyrazy, które znajdzie w słowniku i wydrukować przetworzone zdanie na ekranie.
Wyrazy, które odnalazł, mają być przetłumaczone. 
Wyrazy, których nie odnalazł w słowniku mają być wypisane, tak jak zostały wprowadzone, ale dodatkowo z * na końcu.
Zadbaj o to, żeby pierwsza litera w zdaniu była pisana dużą literą.
Przykład.
Yesterday wieczorem learn się programować*.
'''
def replace_separator(word):
    word = word.replace('!', ' ').replace('/', ' ').replace('|', ' ').replace(';', ' ').replace(':', ' ').replace('.', ' ').replace('\\', ' ').replace('?', ' ')
    word = word.replace(',', ' ').replace('"', ' ').replace('(', ' ').replace(')', ' ').replace('[', ' ').replace(']', ' ').replace('}', ' ').replace('{', ' ')
    return word

pol_eng_dictionary = {
    "dom": "house",
    "samochód": "car",
    "telefon": "phone",
    "kot": "cat",
    "pies": "dog",
    "komputer": "computer",
    "książka": "book",
    "drzewo": "tree",
    "kwiat": "flower",
    "słońce": "sun",
    "księżyc": "moon",
    "morze": "sea",
    "woda": "water",
    "kawa": "coffee",
    "herbata": "tea",
    "jabłko": "apple",
    "banan": "banana",
    "pomarańcza": "orange",
    "zielony": "green",
    "czerwony": "red",
    "jest": "is",
    "życie": "life"    
}

def translate(words):
    new_list = []
    for i in range(len(words)):
        if words[i] in pol_eng_dictionary:
            new_list.append(pol_eng_dictionary[words[i]])
        else:
            new_list.append(words[i] + '*')
    return new_list

def print_result(result_list):
    result = " ".join(result_list)
    result = result.capitalize()
    print(result)

while True:
    sentence = input("Wpisz wyraz lub zdanie do przetłumaczenia na język angielski: ")
    if sentence != '':
        sentence = sentence.lower()
        sentence = replace_separator(sentence)
        separate_words = sentence.split()
        whole_list = translate(separate_words)
        print_result(whole_list)        
    else:
        break