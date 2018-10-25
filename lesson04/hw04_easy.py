# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list_in = [1, 2, 4, 0]
result = list(i**2 for i in list_in)
print(result)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ["apple", "orange", "plum", "peach" , "pear"]
fruits2 = ["plum", "apple", "mango", "quince", "peach" ]
result = []
for i in fruits1:
	for j in fruits2:
		if i == j:
			result.append(i)
print(result)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

list_in = [random.randint(-1000, 1000) for i in range(0, 20)]
print(list_in)
result = list(filter(lambda i: i > 0 and i % 3 == 0 and i % 4 != 0, list_in))
print(result)
