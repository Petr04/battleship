from random import choice

from field import Field
from result import Result

class Player:
	def __init__(self, size):
		self.field = Field(size)

		self.killed = Field(size)
		self.damaged = set()
		self.miss = set()

		self.x = x
		self.y = y

		self.all = set()
		for i in range(self.x-1):
			for j in range(self.y-1):
				self.all.add((i, j))

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
			self.damaged.add((x, y))
			return Result.DAMAGE


		print(self.damaged)
		self.killed |= self.damaged
		self.damaged = set()

		if self.killed == enemy.field:
			return Result.WIN

		return Result.KILL
