from random import choice

from result import Result
from near import near_group
from invert import invert

class Player:
	# Заменить set на Field
	# Сделать метод, который принимает клетку, которую атакуешь, и возвращает результат
	# Сделать приватными некоторые члены класса (например, self.field)
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

		self.fail = False # Для лога

	def __str__(self):
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
		bad = set()

		for ship_type in range(ship_count, 0, -1):
			ship_instance = 0
			while ship_instance < ship_count - ship_type + 1:

				first_set = invert(near_group(self.field, base=True, diagonals=True) | bad)
				if not first_set: # Протестировать
					self.generate()
					return

				new = {choice(list(first_set))}

				for _ in range(ship_type-1):
					cells = near_group(new, base=False, diagonals=False) - \
						(bad | near_group(self.field, base=True, diagonals=True))
					if not cells:
						ship_instance -= 1
						bad |= new
						new.clear()
						break

					new.add(choice(list(cells)))

				self.field |= new
				ship_instance += 1

	def attack(self, enemy):
		empty = (self.miss | near_group(self.killed, diagonals=True, base=True))

		print(empty, self.all - empty, sep='\n')

		if not self.damaged:
			x, y = choice(list( enemy.all - empty ))
		else:
			x, y = choice(list( near_group(self.damaged, diagonals=False,
				base=False) - empty ))

		if not (x, y) in enemy.field:
			self.miss.add((x, y))
			return Result.MISS

		self.damaged.add((x, y))
		if len( near_group(self.damaged, diagonals=False, base=False) & enemy.field ) != 0:
			return Result.DAMAGE

		self.killed |= self.damaged
		self.damaged = set()

		# values = (
		# 	'empty', 'empty == self.all'
		# )

		# for out in values:
		# 	print('{}: {}'.format(out, eval(out)))

		if self.killed == enemy.field:
			return Result.WIN

		return Result.KILL
