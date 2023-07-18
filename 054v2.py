'''
Twoim zadaniem jest stworzenie WŁASNEJ funkcji substring. Nie używaj systemowej, tylko napisz ją od zera (nie używaj slice(), ani [x:y])
A jak już zaimplementujesz, wykonaj przy jej pomocy następujące zadania testowe:
1. Z "Zero To Junior" wyciągnij 4 pierwsze znaki
2. Z "Zero To Junior" wyciągnij 5 ostatnich znaków
3. Znajdź w "Zero To Junior" ciąg "To" i pobierz wszystkie znaki od litery T do końca
4. Wyciągnij z "Zero To Junior" znaki od 3 do 8
'''

def substring(string, index):
    index = check_colon(index)
    index = check_string(index)
    index = check_negative_indexing(index)
    for i in range(index[0], index[1]):
        print(string[i], end="")
    print("")

def check_negative_indexing(i):
    if i[0] < 0:
        i[0] = int(len(word) + i[0])
    else:
        i[0] = i[0]
    if i[1] < 0:
        i[1] = int(len(word) + i[1])
    else:
        i[1] = i[1]
    return i

def check_string(i):
    if type(i[0]) is str:
        i[0] = word.index(i[0])
    else:
        i[0] = i[0]
    if type(i[1]) is str:
        i[1] = word.index(i[1])
    else:
        i[1] = i[1]
    return i

def check_colon(i):
    if i[0] == ":":
        i[0] = 0
    else:
        i[0] = i[0]
    if i[1] == ":":
        i[1] = len(word)
    else:
        i[1] = i[1]
    return i

test = [[0, 4], [-5, ":"], ["To", ":"], [3, 9]]
word = "Zero To Junior"

for i in test:    
    substring(word, i)