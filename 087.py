'''
Mając listę uczniów i ich ocen, użyj list comprehensions, 
aby utworzyć nową listę z uczniami, którzy otrzymali ocenę co najmniej 4.0.
Następnie, używając dictionary comprehensions, utwórz słownik, 
gdzie kluczem będzie imię ucznia, a wartością jego ocena.
'''

students = [("Ania", 3.5), ("Kamil", 4.5), ("Ola", 4.0), ("Piotr", 5.0), ("Ewa", 3.0)]

list_comprehension = [(student, score) for student, score in students if score >= 4.0]
print(list_comprehension)
dict_comprehension = {student: score for student, score in students}
print(dict_comprehension)