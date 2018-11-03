# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Tringle:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def get_lengths(self):
		a_len = ((self.a[0] - self.b[0])**2 + (self.a[1] - self.b[1])**2)**(1/2)
		b_len = ((self.b[0] - self.c[0])**2 + (self.b[1] - self.c[1])**2)**(1/2)
		c_len = ((self.c[0] - self.a[0])**2 + (self.c[1] - self.a[1])**2)**(1/2)
		return (a_len, b_len, c_len)

	def get_perimetr(self):
		heights = self.get_lengths()
		p = heights[0] + heights[1] + heights[2]
		return p

	# по формуле определителя второго порядка
	def get_square(self):
		x1 = self.a[0] - self.c[0]
		x2 = self.b[0] - self.c[0]
		y1 = self.a[1] - self.c[1]
		y2 = self.b[1] - self.c[1]
		s = abs(x1 * y2 - x2 * y1) / 2
		return s

	def get_height(self):
		heights = self.get_lengths()
		p = (heights[0] + heights[1] + heights[2]) / 2
		h = (2 * (p * (p - heights[0]) * (p - heights[1]) * (p - heights[2]))**(1/2)) / heights[0]
		return h
	
tringle = Tringle((1,2), (4,5), (5,4))
print("Площадь: ", tringle.get_square())
print("Высота: ", tringle.get_height())
print("Периметр: ", tringle.get_perimetr())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class EqualBarrel:
	def __init__(self, a, b, c, d):
		self._a = a
		self._b = b
		self._c = c
		self._d = d

	def _vector(self, point1, point2):
		dx = point2[0] - point1[0]
		dy = point2[1] - point1[1]
		if dy == 0:
			k = 0
		else:
			k = round(dx / dy, 1)
		length = round((dx**2 + dy**2)**(1/2), 1)
		return {
			"p1": point1,
			"p2": point2,
			"vx": dx,
			"vy": dy,
			"vk": k,
			"length": length
		}

	def _get_parallel_sides(self):
		if(abs(self.AB["vk"]) == abs(self.CD["vk"]) and self.BC["length"] == self.DA["length"]):
			return ((self.AB, self.CD), (self.BC, self.DA))
		if(abs(self.BC["vk"]) == abs(self.DA["vk"]) and self.AB["length"] == self.BC["length"]):
			return ((self.BC, self.DA), (self.AB, self.CD))
		return None

	@property
	def A(self):
		return self._a

	@property
	def B(self):
		return self._b

	@property
	def C(self):
		return self._c
	
	@property
	def D(self):
		return self._d

	@property
	def AB(self):
		return self._vector(self._a, self._b)

	@property
	def BC(self):
		return self._vector(self._b, self._c)
	
	@property
	def CD(self):
		return self._vector(self._c, self._d)

	@property
	def DA(self):
		return self._vector(self._d, self._a)

	def is_equal_barrel(self):
		sides = self._get_parallel_sides()
		if sides == None:
			return False
		return True
	
	def get_perimetr(self):
		if(not self.is_equal_barrel()):
			return None
		p = self.AB["length"] + self.BC["length"] + self.CD["length"] + self.DA["length"]
		return round(p, 1)

	def get_square(self):
		if(not self.is_equal_barrel()):
			return None
		sides = self._get_parallel_sides()
		s = (sides[0][0]["length"] * sides[0][1]["length"])**(0.5) * ((sides[0][0]["length"] + sides[0][1]["length"]) / 2)
		return round(s, 1)

barrel = EqualBarrel((0,0), (5,0), (4,2), (1,2))
print("Является: ", str(barrel.is_equal_barrel()))
print("Периметр: ", barrel.get_perimetr())
print("Площадь", barrel.get_square())

