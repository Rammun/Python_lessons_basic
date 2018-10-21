# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

# время уже жалко

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

dir_in = "data"
dir_out = "data\\out"

def read_data_from_file(path):
	result = []
	with open(path, 'r', encoding='UTF-8') as f:
		first_line = True		
		for line in f:
			if first_line == True:
				first_line = False
				continue		
			if(len(line) > 0 and line != "\n"):
				row = list(filter(lambda x: x != "" and x != "\n", line.replace("\n", "").split(" ")))
				result.append(row)
	return result

workers = {}
result = read_data_from_file(os.path.join(dir_in, "workers"))
for row in result:
	workers[(row[0], row[1])] = { "salary": int(row[2]), "position": row[3], "rate": int(row[4]) }

hours = {}
result = read_data_from_file(os.path.join(dir_in, "hours_of"))
for row in result:
	hours[(row[0], row[1])] = int(row[2])

with open(os.path.join(dir_out, "register.txt"), 'a', encoding='UTF-8') as f:
	f.write("Имя         Фамилия     Зарплата\n\n")
	for fullname in hours:
		if(workers.get(fullname) != None):
			employee = workers[fullname]
			cost_one_hour = employee["salary"] / employee["rate"]
			excess = hours[fullname] - employee["salary"]
			if(excess > 0):
				current_salary = employee["rate"] * cost_one_hour + excess * cost_one_hour * 2
			else:
				current_salary = hours[fullname] * cost_one_hour
			row = f"{fullname[0]:<12}{fullname[1]:<12}{current_salary:.2f}\n"
			f.write(row)

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import os

dir_in = "data"
dir_out = "out"
filename = "fruits.txt"
path = os.path.join(dir_in, filename)
data = {}

with open(path, 'r', encoding='UTF-8') as f:
	for line in f:
		if(len(line) > 0 and line != "\n"):
			first_letter = line[0].upper()
			if(data.get(first_letter) == None):
				data[first_letter] = []
			data[first_letter].append(line)

for key in data:
	_filename = f"fruits_{key}.txt"
	with open(os.path.join(dir_in, dir_out, _filename), 'a', encoding='UTF-8', ) as f:
		for line in data[key]:
			f.write(line)


