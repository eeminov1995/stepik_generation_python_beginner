# Напишите программу вывода на экран трех последовательно идущих чисел, каждое на отдельной строке. Первое число вводит пользователь, остальные числа вычисляются в программе.

# Формат входных данных
# На вход программе подается одно целое число.

# Формат выходных данных
# Программа должна вывести три последовательно идущих числа в соответствии с условием задачи.

# Тестовые данные 🟢
# Sample Input 1:

# 8
# Sample Output 1:

# 8
# 9
# 10

# put your python code here
a = int(input())
b = a + 1
c = a + 2
print(a, b, c, sep="\n")