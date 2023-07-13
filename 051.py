'''
Napisz aplikację, która:
- pobierze wiele linii, wpisanego na ekranie tekstu
- policzy wszystkie wyrazy i wypisz ich ilość na ekranie
'''

def replace_separator(word):
    word = word.replace('!', ' ').replace('/', ' ').replace('|', ' ').replace(';', ' ').replace(':', ' ').replace('.', ' ').replace('\\', ' ').replace('?', ' ')
    word = word.replace(',', ' ')
    return word

def add_to_one_list(new_list, initial_list):
    for x in new_list:
        initial_list.append(x)
    return initial_list

whole_list = []
while True:
    user_input = ""
    user_input = input("Wprowadź dowolną ilość wyrazów: ")
    if user_input != '':
        user_input = replace_separator(user_input)
        separate_words = user_input.split()
        whole_list = add_to_one_list(separate_words, whole_list)
    else:        
        whole_input_set = set(whole_list)
        print(len(whole_input_set), ": ", whole_input_set)
        break