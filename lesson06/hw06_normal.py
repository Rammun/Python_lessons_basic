# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Programm:
	def __init__(self):
		self._school = self.init()
		self._repository = Repository(self._school)
	
	def menu(self):
		print("\n1. Получить полный список всех классов школы")
		print("2. Получить список всех учеников в указанном классе")
		print("3. Получить список всех предметов указанного ученика")
		print("4. Узнать ФИО родителей указанного ученика")
		print("5. Получить список всех учителей, преподающих в указанном классе")
		print("6. Выход")

	def start(self):
		actions = {
			"1": self._get_class_numbers,
			"2": self._get_students_by_class,
			"3": self._get_subjects_by_student,
			"4": self._get_parents_fullname,
			"5": self._get_teachers_by_class,
			"6": None
		}

		while True:
			self.menu()
			selection = input("Ваш запрос: ")
			func = actions.get(selection, "Not known")
			if func == "Not known":
				print("Неизвестная комманда")
				continue
			if func == None:
				break
			#print("\n")
			func()

	def init(self):
		student1 = Student("Соколов", Mother("Маша"), Father("Саша"))
		student2 = Student("Иванов", Mother("Даша"), Father("Паша"))
		student3 = Student("Петров", Mother("Лена"), Father("Гена"))
		student4 = Student("Баширов", Mother("Зина"), Father("Дима"))
		student5 = Student("Васечкин", Mother("Аня"), Father("Ваня"))

		teacher1 = Teacher("Дарья Ивановна", Subject("Математика"))
		teacher2 = Teacher("Андрей Сергеевич", Subject("Физкультура"))
		teacher3 = Teacher("Александр Павлович", Subject("Информатика"))
		teacher4 = Teacher("Валентина Игоревна", Subject("Химия"))
		teacher5 = Teacher("Екатерина Михайловна", Subject("Физика"))

		class_7b = Class("7-Б")
		class_7b.students.extend([student1, student2, student3])
		class_7b.teachers.extend([teacher1, teacher2])

		class_5d = Class("5-Д")
		class_5d.students.extend([student4, student5])
		class_5d.teachers.extend([teacher3, teacher4, teacher5])

		school = School()
		school.classes.extend([class_7b, class_5d])
		return school

	def _get_class_numbers(self):
		class_numbers = self._repository.get_class_numbers()
		print("\nНомера классов:")
		for number in class_numbers:
			print(number) 

	def _get_students_by_class(self):
		class_name = input("Номер класса: ")
		students = self._repository.get_students_by_class(class_name)
		print("\nУченики класса ", class_name, ":")
		for name in students:
			print(name) 

	def _get_subjects_by_student(self):
		student_name = input("Имя студента: ")
		subjects = self._repository.get_subjects_by_student(student_name)
		print("\nПредметы:")
		for subject in subjects:
			print(subject)

	def _get_parents_fullname(self):
		student_name = input("Имя студента: ")
		parents = self._repository.get_parents_fullname(student_name)
		print("\nРодители:")
		print("Мама: ", parents["mother"])
		print("Папа: ", parents["father"])

	def _get_teachers_by_class(self):
		class_number = input("Номер класса: ")
		teachers = self._repository.get_teachers_by_class(class_number)
		for t in teachers:
			print(t)

class Repository:
	def __init__(self, school):
		self._school = school

	def _get_class_by_number(self, class_number):
		for cl in self._school.classes:
			if cl.number == class_number:
				return cl
		return None
	
	def get_class_numbers(self):
		numbers = [cl.number for cl in self._school.classes]
		return numbers

	def get_students_by_class(self, class_number):
		cl = self._get_class_by_number(class_number)
		if(cl == None):
			return []
		student_names = [st.name for st in cl.students]
		return student_names

	def get_subjects_by_student(self, student_name):
		for cl in self._school.classes:
			if student_name in [s.name for s in cl.students]:
				subjects =  [t.subject.name for t in cl.teachers]
				return subjects
		return []

	def get_parents_fullname(self, student_name):
		for cl in self._school.classes:
			for st in cl.students:
				if st.name == student_name:
					return {
						"mother": st.mother.name,
						"father": st.father.name
					}
		return None
	
	def get_teachers_by_class(self, class_number):
		cl = self._get_class_by_number(class_number)
		if(cl == None):
			return []
		teachers = [t.name for t in cl.teachers]
		return teachers


class School:
	def __init__(self):
		self._classes = []

	@property	
	def classes(self):
		return self._classes

class Class:
	def __init__(self, number):
		self._number = number
		self._students = []
		self._teachers = []

	@property
	def number(self):
		return self._number

	@property
	def students(self):
		return self._students

	@property
	def teachers(self):
		return self._teachers

class Subject:
	def __init__(self, name):
		self.name = name

class Teacher:
	def __init__(self, name, subject):
		self.name = name
		self.subject = subject

class Student:
	def __init__(self, name, mother, father):
		self.name = name
		self.mother = mother
		self.father = father
	
class Mother:
	def __init__(self, name):
		self.name = name

class Father:
	def __init__(self, name):
		self.name = name

programm = Programm()
programm.start()

""" 
student1 = Student("Соколов", Mother("Маша"), Father("Саша"))
student2 = Student("Иванов", Mother("Даша"), Father("Паша"))
student3 = Student("Петров", Mother("Лена"), Father("Гена"))
student4 = Student("Баширов", Mother("Зина"), Father("Дима"))
student5 = Student("Васечкин", Mother("Аня"), Father("Ваня"))

teacher1 = Teacher("Дарья Ивановна", Subject("Математика"))
teacher2 = Teacher("Андрей Сергеевич", Subject("Физкультура"))
teacher3 = Teacher("Александр Павлович", Subject("Информатика"))
teacher4 = Teacher("Валентина Игоревна", Subject("Химия"))
teacher5 = Teacher("Екатерина Михайловна", Subject("Физика"))

class_7b = Class("7-Б")
class_7b.students.extend([student1, student2, student3])
class_7b.teachers.extend([teacher1, teacher2])

class_5d = Class("5-Д")
class_5d.students.extend([student4, student5])
class_5d.teachers.extend([teacher3, teacher4, teacher5])

school = School()
school.classes.extend([class_7b, class_5d])

for cl in school.classes:
	print("\nКласс: ", cl.number)
	print("Учителя:")
	for t in cl.teachers:
		print(t.name, "  ", t.subject.name)
	print("Студенты:")
	for s in cl.students:
		print(s.name, "  мама: ", s.mother.name, "  папа: ", s.father.name)  """
