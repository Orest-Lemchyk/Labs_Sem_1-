#Лабораторні роботи з дисципліни "Алгоритмізація та програмування"
 #Виконав: Лемчик Орест Юрійович (ІР-14)
 #Лабораторна робота №1 (Варіант 11)
 #Створити змінну присвоїти їй назву і вивести рядок. Порахувати вираз.

from math import cos as cosinus , sqrt

sport = "Table tenis"
print(sport)

is_student, is_teacher = False, True
print(is_student and not is_teacher)

is_hot, is_cold = True, False
print(is_hot or is_cold)

x, y = 15.241, 7.118
result = (3 *sqrt(x + y**3)) / (y ** (1 / 3)) + (3 / (4 * x)) * cosinus(y)
print(result)