from loto import *
#from ui import *

class Game:
	def __init__(self):
		# settings
		self._max_players = 6
		self._kegs_count = 90
		self._cards_count = 20
		self._default_players = [("Компьютер", True), ("Игрок", False)]

		self._loto = None
		self._ui = None

	def _init(self):
		self._loto = Loto(self._max_players, self._kegs_count, self._cards_count)
		#self._ui = UI()

	def start(self):
		while True:
			self._init()

			for player in self._default_players:
				is_add = self._loto.add_player(player[0], player[1])
				if is_add:
					print(f"Игрок '{player[0]}' добавлен...")
				else:
					print(f"Достигнут предел кол-ва игроков: {self._max_players}")
					break

			self._game_process()

			inp = input("Сыграть еще раз? (д/...)")
			if (inp != "д"):
				break
	
	def _game_process(self):
		self._loto.start()

		result_round_move = True
		while(result_round_move):
			result_round_move = self._loto.round_move()



