'''
Masz przez 3 tygodnie, wykonywać codziennie pięć konkretnych tasków.
Zadanie A, Zadanie B, Zadanie C, Zadanie D i Zadanie E
Przygotuj kod, który wypisze na ekranie listę zadań w następujący sposób.
Dzień tygodnia - numer zadania - opis zadania
1 - 1 - Zadanie A
1 - 2 - Zadanie B
1 - 3 - Zadanie C
1 - 4 - Zadanie D
1 - 5 - Zadanie E
2 - 1 - Zadanie A
2 - 2 - Zadanie B
Itd.
'''

dayNumber = 1 
taskNumber = 0
taskDescription = ["Zadanie A", "Zadanie B", "Zadania C", "Zadanie D", "Zadanie E"]

while dayNumber <= 21:
    if taskNumber == 5:
        taskNumber = 0
        dayNumber = dayNumber + 1
    else:
        print(dayNumber, " - ", taskNumber + 1, " - ", taskDescription[taskNumber])
        taskNumber = taskNumber + 1
