import random
from interface import Result

from near import near_group

class Gameboard:
	def __init__(self, x=10, y=10):
		self.field = set()

		self.killed = set()
		self.damaged = set()
		self.miss = set()

		self.x = x
		self.y = y

		self.all = set()
		for i in range(self.x-1):
			for j in range(self.y-1):
				self.all.add((i, j))

		self.fail = False # Для информации

	def __repr__(self):
		ret = ''
		for i in range(self.x):
			for j in range(self.y):
				if (i, j) in self.field:
					ret += 'X'
				else:
					ret += ' '

			ret += '\n'

		return ret

	def generate(self, ship_count=4):

		for ship_type in range(ship_count):
			ship_type += 1

			for ship_copy in range(ship_count - (ship_type - 1)):

				first_set = list(self.all - near_group(self.field, diagonals=True, base=True))
				# Потенциальные first

				while True:
					first = random.choice(list(first_set)) # Выбирать из доступных

					print(first, ship_type)
					print('----------')

					new = {first} # Ячейки нового корабля

					for ship_cell in range(ship_type-1):

						near = near_group(new, base=False, diagonals=False)
						print('near: {}'.format(near))

						available = near - near_group(self.field, base=True, diagonals=True)
						if len(available) == 0:
							print('Ступор')
							self.fail = True
							break

						new.add(random.choice(list(available)))

					if len(new) == ship_type:
						break

					first_set.remove(first)

				print('Result: {}'.format(new))
				self.field |= new
				print()

	def attack(self, enemy):
		empty = (self.miss | near_group(self.killed, diagonals=True, base=True))
		if not self.damaged:
			x, y = random.choice(list( enemy.all - empty ))
		else:
			x, y = random.choice(list( near_group(self.damaged, diagonals=False,
				base=False) - empty ))

		print(' на {}: {}'.format((x, y), (x, y) in enemy.field)) # Для test.py (ходит на ...)

		if not (x, y) in enemy.field:
			self.miss.add((x, y))
			return Result.MISS

		self.damaged.add((x, y))
		if len( near_group(self.damaged, diagonals=False, base=False) & enemy.field ) != 0:
			self.damaged.add((x, y))
			return Result.DAMAGE


		print(self.damaged)
		self.killed |= self.damaged
		self.damaged = set()

		if self.killed == enemy.field:
			return Result.WIN

		return Result.KILL
