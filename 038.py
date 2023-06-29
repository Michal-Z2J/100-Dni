'''
Zsumuj liczby parzyste (i oczywiście wydrukuj rezultat)
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
positiveNumbersSum = 0

for x in numbers:
    if x % 2 == 0:
        positiveNumbersSum += x
print(positiveNumbersSum)
