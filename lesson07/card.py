from random import randint

class Card:
	def __init__(self):
		self._numbers = self._get_numbers()

	def _get_numbers(self):
		numbers = [[None for i in range(9)] for j in range(3)]
		values = list(range(1, 90))
		for j in range(3):
			temp = []
			for i in range(5):
				while(True):
					rnd = randint(0, len(values) - 1)
					if(values[rnd] // 10 not in temp):
						break
				number = values.pop(rnd)
				index = number // 10
				temp.append(index)
				numbers[j][index] = { "number": number, "active": True }
		return numbers

	def _get_chars(self, value):
		if value == None:
			cell = "  "
		elif value["active"] == False:
			cell = "--"
		else:
			cell = "{:>2}".format(value["number"])
		return cell

	def show_card(self, title):
		count = int((35 - len(title)) / 2)
		print("-" * count + title + "-" * count)
		for j in range(3):
			row = "  ".join(map(lambda x: self._get_chars(x), self._numbers[j]))
			print(row)
		print("-" * 35)

	def number_is_exists(self, number):
		for j in range(3):
			for i in range(9):
				if(self._numbers[j][i] != None and self._numbers[j][i]["number"] == number):
					return True
		return False

	def try_crossout(self, number):
		for j in range(3):
			for i in range(9):
				if(self._numbers[j][i] != None and self._numbers[j][i]["number"] == number):
					self._numbers[j][i]["active"] = False
					return True
		return False

	def is_crossout_all(self):
		for j in range(3):
			for i in range(9):
				if(self._numbers[j][i] != None and self._numbers[j][i]["active"] == True):
					return False
		return True

	@property
	def get_numbers(self):
		return self._numbers