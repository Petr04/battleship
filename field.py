import numpy as np
import random

class Field:
	def __init__(self, size, ship_count=4, elements=set()):
		self.size = size
		self.ship_count = ship_count

		self.field = np.full(self.size, False)
		if elements:
			for i in range(self.size[0]):
				for j in range(self.size[1]):
					self.field[i][j] = (i, j) in elements

	def __str__(self):
		ret = ''

		for i in self.field:
			for j in i:
				ret += (' ', 'X')[int(j)]
			ret += '\n'

		return ret

	def elements(self):
		ret = set()

		for i in self.field:
			for j in i:
				if j:
					ret.add((i, j))

		return ret

	def clear(self):
		self.field = np.full(self.size, False)

	def near(self, base, diagonals):
		ret = Field(self.size)

		for i in range(self.size[0]):
			for j in range(self.size[1]):

				if not self.field[i][j]:
					continue

				d = (-1, 0, 1)
				for d_i in d:
					for d_j in d:

						new_i, new_j = [sum(pair) for pair in zip((i, j), (d_i, d_j))]

						for new, s in zip((new_i, new_j), self.size):
							if new not in range(s):
								break
						else:
							if ( (not base) and self.field[new_i][new_j] ) or \
								( (not diagonals) and (0 not in (d_i, d_j)) ) :
								continue

							ret.field[new_i][new_j] = True

		return ret

	def generate(self):
		bad = set()

		for ship_type in range(self.ship_count, 0, -1):
			ship_instance = 0
			while ship_instance < self.ship_count - ship_type + 1:

				first_set = invert(near_group(self.field, base=True, diagonals=True) | bad)
				if not first_set: # Протестировать
					self.generate()
					return

				new = {random.choice(list(first_set))}

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

if __name__ == '__main__':
	f = Field((10, 10))
	f.generate()
	print(f)
