'''
Wypisz na ekranie wyniki tabliczki mnożenia od 1 do 100.
Zrób to zadanie, ale formatując wyjściowy rezultat w tablicy 10 x 10.
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1, 11):
    for x in numbers:
        print(x*i,end='\t')
    print("\n")
