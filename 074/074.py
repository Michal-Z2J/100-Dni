'''
Stwórz moduł o nazwie text, który zawiera następujące funkcje:
- small_letters(s): Zmienia wszystkie litery w tekście na małe.
- large_letters(s): Zmienia wszystkie litery w tekście na wielkie.
- Następnie zaimportuj te funkcje do głównego pliku i użyj ich, aby zmienić tekst wprowadzony przez użytkownika.
'''
from text import small_letters as small
from text import large_letters as large

user_text = input("Wprowadź tekst do zamiany na małe i duże litery: ")

print(small(user_text))
print(large(user_text))
