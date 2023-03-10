# Напишите программу, вычисляющую объём куба и площадь его полной поверхности, по введённому значению длины ребра.

# Формат входных данных
# На вход программе подается одно целое число – длина ребра.

# Формат выходных данных
# Программа должна вывести текст и числа в соответствии с условием задачи.

# Примечание. Объём куба и площадь полной поверхности можно вычислить по формулам V = a^3, S = 6a^2

# Тестовые данные 🟢
# Sample Input 1:

# 25
# Sample Output 1:

# Объем = 15625
# Площадь полной поверхности = 3750

# put your python code here
dr = int(input())
v = dr**3
s = 6 * dr**2
print("Объём = " + str(v), "Площадь полной поверхности = " + str(s), sep="\n")
