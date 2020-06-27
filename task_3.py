# homework les 1.3
# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = input('Введите любое число(n): ')
print(f'Сумма {user_number} + {user_number * 2} + {user_number * 3} = ')

print(int(user_number) + (int(user_number) * 11) + (int(user_number) * 111))