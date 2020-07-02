# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict

list_seasons = ['зиме', 'весне', 'лету', 'осени']
dict_seasons = {1: list_seasons[0], 2: list_seasons[1], 3: list_seasons[2], 4: list_seasons[3]}

user_month = int(input('Введите число любого месяца(от 1 до 12):\n'))

if user_month == 1 or user_month == 12 or user_month == 2:
    print(user_month, '-й месяц относится к', dict_seasons.get(1))

elif user_month == 3 or user_month == 4 or user_month == 5:
    print(user_month, '-й месяц относится к', dict_seasons.get(2))

elif user_month == 6 or user_month == 7 or user_month == 8:
    print(user_month, '-й месяц относится к', dict_seasons.get(3))

elif user_month == 9 or user_month == 10 or user_month == 11:
    print(user_month, '-й месяц относится к', dict_seasons.get(4))

else:
    print('Введите цифру месяца от 1 до 12')