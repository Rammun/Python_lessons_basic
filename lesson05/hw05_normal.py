# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import shutil

def menu():
	print("1. Перейти в папку")
	print("2. Просмотреть содержимое текущей папки")
	print("3. Удалить папку")
	print("4. Создать папку")
	print("5. Выход")

def get_current_path():
	return os.getcwd()

def go_to_folder():
	print("--- Перейти в папку ---")
	path = input("Путь: ")
	if not os.path.exists(dirname):
		print("Невозможно перейти!")
		return
	os.chdir(path)
	print("--- Успешно перешел")

def view_contents():
	print("--- Просмотреть содержимое ---")
	current_directory = os.getcwd()
	names = [name for name in os.listdir(current_directory)]
	for d in names:
		print(d)
	print("--- Успешно")

def delete_folder():
	print("--- Удалить папку ---")
	dirname = input("Имя папки: ")
	if not os.path.exists(dirname):
		print("В текущем каталоге папки с таким именем не существует!")
		return
	os.rmdir(dirname)
	print("--- Успешно удалено")

def create_folder():
	print("--- Создать папку ---")
	dirname = input("Имя папки: ")
	if os.path.exists(dirname):
		print("В текущем каталоге папка с таким именем уже существует!")
		return
	os.makedirs(dirname)
	print("--- Успешно создано")

def start():
	actions = {
		"1": go_to_folder,
		"2": view_contents,
		"3": delete_folder,
		"4": create_folder,
		"5": None
	}
	while(True):
		print("\n")
		print(get_current_path())
		menu()
		selection = input("Ваше действие:")
		func = actions.get(selection, "Not known")
		if func == "Not known":
			print("Неизвестная комманда")
			continue
		if func == None:
			break
		print("\n")
		func()

start()


