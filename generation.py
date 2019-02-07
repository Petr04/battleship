from random import choice # В gameboard.py потом заменить в коде использование random

from gameboard import Gameboard
from near import near_group
from invert import invert

class NewGameboard(Gameboard):

	def generate(self, ship_count=4):
		bad = set()

		for ship_type in range(ship_count, 0, -1):
			for ship_instance in range(ship_count - ship_type + 1):

				first_set = invert(near_group(self.field, base=True, diagonals=True) | bad)
				if not first_set: # Протестировать
					self.generate()
					print('lol')
					return

				new = {choice(list(first_set))}

				for ship_cell in range(ship_type):
					cells = near_group(new, base=False, diagonals=False) - bad
					if not cells:
						ship_instance -= 1
						bad |= new
						break

					new.add(choice(list(cells)))

				self.field |= new

p = NewGameboard()
p.generate()
print(p)
