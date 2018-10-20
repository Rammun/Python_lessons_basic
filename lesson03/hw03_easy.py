# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    int_part = number // 1
    fract_part = get_fract_part(number, ndigits)
    difference = get_fract_part(number, ndigits + 1) - fract_part * 10
    if(difference < 5):
        return int_part + fract_part / 10**ndigits
    return int_part + (fract_part + 1) / 10**ndigits

def get_fract_part(number, ndigits):
    return number % 1 * (10**ndigits)  // 1

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    number_str = str(ticket_number)
    length = len(number_str)
    if(length % 2 == 0):
        half = int(length / 2)
        left = [ int(i) for i in number_str[:half] ]
        right =[ int(i) for i in number_str[half:] ]
        if sum(left) == sum(right):
            return "Счастливый!"
    return "Не счастливый :("

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436752))
