# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def create_folder(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

create_folder("dir_1")
create_folder("dir_2")


def delete_folder(directory):
	if os.path.exists(directory):
		os.rmdir(directory)

delete_folder("dir_1")
delete_folder("dir_2")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

current_directory = os.getcwd()
print ([name for name in os.listdir(current_directory) if os.path.isdir(name)])

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
current_file = os.path.basename(__file__)
shutil.copyfile(current_file, 'copy_' + current_file) 
