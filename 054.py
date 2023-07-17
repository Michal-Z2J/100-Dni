'''
Twoim zadaniem jest stworzenie WŁASNEJ funkcji substring. Nie używaj systemowej, tylko napisz ją od zera (nie używaj slice(), ani [x:y])
A jak już zaimplementujesz, wykonaj przy jej pomocy następujące zadania testowe:
1. Z "Zero To Junior" wyciągnij 4 pierwsze znaki
2. Z "Zero To Junior" wyciągnij 5 ostatnich znaków
3. Znajdź w "Zero To Junior" ciąg "To" i pobierz wszystkie znaki od litery T do końca
4. Wyciągnij z "Zero To Junior" znaki od 3 do 8
'''
word = "Zero To Junior"
test = [[0, 4], [-5, ":"], ["To", ":"], [3, 9]]

def substring(string, slice_from, slice_to):
    for i in range(slice_from, slice_to):
        print(string[i], end="")
    print("")

def check_negative_indexing(index):
    if index[0] < 0:
        start = int(len(word) + index[0])
    else:
        start = index[0]
    if index[1] < 0:
        stop = int(len(word) + index[1])
    else:
        stop = index[1]
    return start, stop

def check_string(word, i):
    if type(i[0]) is str:
        i[0] = word.index(i[0])
    else:
        i[0] = i[0]
    if type(i[1]) is str:
        i[1] = word.index(i[1])
    else:
        i[1] = i[1]
    return i

def check_colon(word, i):
    if i[0] == ":":
        i[0] = 0
    else:
        i[0] = i[0]
    if i[1] == ":":
        i[1] = len(word)
    else:
        i[1] = i[1]
    return i

for i in test:
    i = check_colon(word, i)
    i = check_string(word, i)
    start, stop = check_negative_indexing(i)
    substring(word, start, stop)