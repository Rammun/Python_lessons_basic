# from card import *

class Player:
	def __init__(self, name, is_computer):
		self._name = name
		self._card = None
		self._is_computer = is_computer
		self.point = 0

	def take_card(self, card):
		self._card = card

	def show_card(self):
		title = f" Карточка игрока {self._name} "
		self._card.show_card(title)

	@property
	def get_name(self):
		return self._name

	@property
	def get_card(self):
		return self._card
	
	@property
	def is_computer(self):
		return self._is_computer