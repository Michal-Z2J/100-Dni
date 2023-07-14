'''
Narysuj prostokąt o podanych przez użytkownika rozmiarach.
'''

width = input("Podaj szerokość prostokąta: ")
width = int(width)
height = input("Podaj wysokość prostokąta: ")
height = int(height)
print("\n")

FIRST_LINE = 0
LAST_LINE = height-1
FIRST_ROW = 0
LAST_ROW = width-1

print("Prostokąt pełny: ")
for i in range(height):
    for x in range(width):
        print("*", end="  ")
    print()

print("\n")
print("Prostokąt pusty: ")
for i in range(height):
    if i == FIRST_LINE:
        for x in range(width):            
            print("*", end="  ")
        print()
    if i == LAST_LINE:
        for x in range(width):
            if height == 1:
                break
            else:
                print("*", end="  ")
    if (i > FIRST_LINE and i < LAST_LINE):
        for x in range(width):            
            if x == FIRST_ROW:
                print("*", end="")
            if (x > FIRST_ROW and x < LAST_ROW):
                print(" ", end="  ")
            if x == LAST_ROW:                
                if width == 1:
                    print()
                else:
                    print("  *")