# Задание task_02_03.
#
# Выполнила: Бурмистрова З.В.
# Группа: ЦИБ-251
a = int(input("Ширина форточки: "))
b = int(input("Высота форточки: "))
d = int(input("Диаметр головы: "))
if a > 0 and b > 0 and d > 0:
    fix = 1
    if d + 2 * fix <= a and d + 2 * fix <= b:
        print("Да")
    else:
        print("Нет")
else:
    print("Проверьте ввод")