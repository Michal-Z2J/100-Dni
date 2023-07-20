'''
Stwórz generator hasła.
Hasło musi zawierać co najmniej jedną cyfrę.
Hasło musi zawierać co najmniej jedną dużą literę.
Hasło musi zawierać co najmniej jedną małą literę.
Hasło musi zawierać co najmniej jeden znak specjalny.
Hasło musi mieć między 10 a 15 znaków.
Hasło nie może zawierać znaków "mylących", 1, I, O, 0.
Hint: Wyszukaj w Google: random number generator python
'''
import random

numbers = "23456789"
letters = "abcdefghjkmnopqrstuvwxyz"
symbols = "!#$%&()*+,-./:;<=>?@[\]^_`{|}~"

password = [random.choice(numbers)]
password.append(random.choice(letters)) 
password.append(random.choice(letters.upper())) 
password.append(random.choice(symbols))

for i in range(0, random.randrange(6, 12)):
    password.append(random.choice(letters + letters.upper() + symbols))

random.shuffle(password)
password = "".join(password)
print("Password: ", password, " ,length:", len(password))