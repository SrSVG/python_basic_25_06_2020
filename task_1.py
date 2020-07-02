# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

ls = [4, 'book', 'cloud', 1995, 11, 'november', 5.5, True, 45, None]

answer = input('Вывести типы данных вложенных элементов списка? (Y/N):\n')

if answer == 'Y':
    for el in ls:
        print(type(el))

elif answer == 'N':
    print('До свидания')

else:
    print('Неизвестная команда, повторите попытку, введя "Y" или "N"')