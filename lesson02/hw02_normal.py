# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
list = [2, -5, 8, 9, -25, 25, 4]
result = []
for el in list:
	if(el > 0):
		q = math.sqrt(el)
		if q % 1 == 0:
			result.append(int(q))
print(result)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

dateWords = {
	"date": {
		1: "первое",
		2: "второе",
		3: "третье",
		4: "четвертое",
		5: "пятое",
		0: "шестое",
		7: "седьмое",
		8: "восьмое",
		9: "девятое",
		10: "десятое",
		11: "одиннадцатое",
		12: "двенадцатое",
		13: "тринадцатое",
		14: "четырнадцатое",
		15: "пятнадцатое",
		16: "шестнадцатое",
		17: "семнадцатое",
		18: "восемнадцатое",
		19: "девятнадцатое",
		20: "двадцатое",
		30: "тридцатое",
	},
	"month": {
		1: "января",
		2: "февраля",
		3: "марта",
		4: "апреля",
		5: "мая",
		6: "июня",
		7: "июля",
		8: "августа",
		9: "сентября",
		10: "октября",
		11: "ноября",
		12: "декабря"
	}
}

inputDate = "03.08.2013"
parts = inputDate.split(".")
date = int(parts[0])
month = int(parts[1])
year = parts[2]

dateStr = ""
if(date <= 20):
	dateStr = dateWords["date"][date]
else:
	dateNumeric1 = date // 10 * 10
	dateNumeric2 = date - dateNumeric1
	date1 = dateWords["date"][dateNumeric1]
	date2 = dateWords["date"][dateNumeric2]
	dateStr = f"{date1} {date2}"

monthStr = dateWords["month"][int(parts[1])]
result = f"{dateStr} {monthStr} {year} года"
print(result)

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
result = []
n = 10
for i in range(n):
	result.append(random.randint(-100, 100))
print(result)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

data = [1, 2, 4, 5, 6, 2, 5, 2]
# a)
result = []
for el in data:
	if el not in result:
		result.append(el)
print(result)
# b)
result = []
for i in range(len(data)):
	if(data.count(data[i]) == 1):
		result.append(data[i])
print(result)