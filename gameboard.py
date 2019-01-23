import random
import enum

# Поменять на import ...
from near import *
from convert import *

class Gameboard:
	def __init__(self, x=10, y=10):
		self.field = set()

		self.killed = set()
		self.damaged = set() # Раненый корабль
		self.miss = set()

		self.x = x
		self.y = y

		self.all = set()
		for i in range(self.x-1):
			for j in range(self.y-1):
				self.all.add((i, j))

		self.fail = False # Для информации

	def __repr__(self):
		field = coords_to_field(self.field)
		ret = ''

		for i in field:
			for j in i:
				ret += ((' ', 'X')[j])
			ret += ('\n')

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

						near = near_group(new)
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
		if not self.damaged:
			x, y = random.choice(list( enemy.all - (self.miss & near_group(self.killed, diagonals=True, base=True)) ))
		else:
			x, y = random.choice(list( near_group(self.damaged, diagonals=False,
				base=False) - (self.miss & near_group(self.killed, diagonals=True, base=True)) ))

		print(' на {}: {}'.format((x, y), (x, y) in enemy.field)) # Для test.py

		if not (x, y) in enemy.field:
			self.miss.add((x, y))
			return 0 # Мимо

		if near((x, y), diagonals=False, base=False) & (enemy.field - self.damaged):
			print(near((x, y), diagonals=False, base=False) - (enemy.field - self.damaged))
			self.damaged.add((x, y))
			return 1 # Ранил


		print({(x, y)} | self.damaged)
		self.killed |= self.damaged | {(x, y)}
		self.damaged = set()

		if self.killed == enemy.field:
			return 3 # Победил

		return 2 # Убил

def make_coord(self, str_coord): # a1 -> (0, 0) переместить в main
	if len(str_coord) != 2:
		return None

	str_coord = str_coord.lower()
	ret = (ord(str_coord[0])-97, int(str_coord[1])-1)

	for i in range(len(ret)):
		if not (0 <= ret[i] <= (self.x, self.y)[i]): # Проверить, нужно ли здесь вычитать 1
													 # или поставить < вместо <=
			return None

	return ret
