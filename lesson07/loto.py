from random import randint
from card import *
from player import *

class Loto:
	def __init__(self, max_players, kegs_count, cards_count):
		self._max_players = max_players
		self._kegs_count = kegs_count
		self._cards_count = cards_count

		self._kegs = []
		self._cards = []
		self._current_player = 0
		self._turn_number = 0
		self.players = []

		self._init_loto()

	def _init_loto(self):
		self._kegs = list(range(1, self._kegs_count + 1))
		self._cards = []
		self._current_player = 0
		self._turn_number = 0

	def get_keg(self):
		rnd_index = randint(0, len(self._kegs) - 1)
		keg = self._kegs.pop(rnd_index)
		return keg

	def add_player(self, name, is_computer):
		if(len(self.players) > self._max_players):
			return False
		self.players.append(Player(name, is_computer))
		return True

	def start(self):
		self._init_loto()
		for i in range(self._cards_count):
			self._cards.append(Card())
		for player in self.players:
			player.take_card(self._cards.pop())

	def move(self, player, keg):
		decision = ""
		is_exists = player.get_card.number_is_exists(keg)
		if (player.is_computer == True):
			if (is_exists == True):
				decision = "з"
				description = "зачеркнуть"
			else:
				decision = "п"
				description = "продолжить"
			print(f"Игрок {player.get_name} выбрал '{description}'")
		else:
			while(True):
				decision = input("Зачеркнуть или продолжить? (з/п): ")
				if (decision == "з" or decision == "п"):
					break
				print("Недопустимый ответ!")

		result = False
		if (decision == "з"):
			result = player.get_card.try_crossout(keg)
		elif (decision == "п"):
			return not is_exists
		
		return result

	def round_move(self):
		self._turn_number += 1
		keg = self.get_keg()
		print(f"\nХод {self._turn_number}")
		print(f"Бочонок: {keg}")
		for player in self.players:
			print("")
			player.show_card()
			result = self.move(player, keg)
			if(result == False):
				print(f"Игрок {player.get_name} проиграл. Он выбывает из игры.")
				# Здесь нужна логика на выбитие игрока, но пока из расчета только двух игроков
				return False
			is_win = player.get_card.is_crossout_all()
			if(is_win == True):
				print(f"Игрок {player.get_name} выиграл!!!")
				return False
		return True

	def stop(self):
		pass