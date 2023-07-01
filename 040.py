# This Python file uses the following encoding: Windows-1250
import os, sys

"""
Dzisiaj prościutko. Napisz funkcję, która z podanej listy zwróci 
wartość minimalną i maksymalną jednocześnie :)
"""
nums = [99, 5, 1, 1000, 6, -99]

# Wersja z własną funkcją do szukania min/max
def findMinMax(numbers):
    maxNumber = minNumber = numbers[1]
    for x in numbers:
        if x > maxNumber:
            maxNumber = x
        elif x < minNumber:
            minNumber = x
    return (maxNumber, minNumber)

# Krótka wersja
def findMinMaxShort(numbers):
    return (max(numbers), min(numbers))

maximum, minimum = findMinMax(nums)
print("Max:", maximum)
print("Min:", minimum)

maximumShort, minimumShort = findMinMaxShort(nums)
print("Max:", maximumShort)
print("Min:", minimumShort)
