'''
Twoim zadaniem jest napisanie kodu, który:
- Pobierze plik https://zerotojunior.dev/cezar.txt.
- Odszyfruje go (i automatycznie wykryje, że plik jest odszyfrowany).
- Wypisze odszyfrowany tekst na ekranie.
'''
import requests
def replace_char(char_displacement):
    new = []
    for i in text:
        if i in letters:
            shift = letters.index(i) + char_displacement
            if shift >= len(letters):
                shift = abs(len(letters) - shift)
            new.append(letters[shift])
        elif i in letters_upper:
            shift = letters_upper.index(i) + char_displacement
            if shift >= len(letters_upper):
                shift = abs(len(letters_upper) - shift)
            new.append(letters_upper[shift])
        else:
            new.append(i)
    return "".join(new)

def most_numerous_char(text):
    letters_count = {}
    for i in text.lower():
        if i in letters_count:
            letters_count[i] += 1
        elif i not in special_characters:
            letters_count[i] = 1
    return max(letters_count, key = letters_count.get)

def decode_text(text):
    char_displacement = 0
    highest = most_numerous_char(text)
    while highest != "e":
        text = replace_char(char_displacement)
        highest = most_numerous_char(text)
        char_displacement += 1
    return text

url = 'https://zerotojunior.dev/cezar.txt'
response = requests.get(url)

letters = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
letters_upper = letters.upper()
special_characters = " ,.!?:;()\n"

# Sprawdź, czy żądanie zakończyło się sukcesem (kod odpowiedzi 200)
if response.status_code == 200:
    # Odczytaj zawartość pliku, uwzględniając odpowiednie kodowanie znaków
    text = response.content.decode('UTF-8', errors='ignore')
    text_new = decode_text(text)
    print("Pobrany tekst:")
    print(text_new)
else:
    print(f"Błąd pobierania pliku: {response.status_code}")