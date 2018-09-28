import random

from convert import field_to_coords

size = 10

def near(cell, diagonals=False, base=False):
	ret = set()
	delta = (-1, 0, 1)
	for i in delta:
		for j in delta:
			if not((not diagonals) and (not (0 in (i, j)))):
				ret.add((cell[0]+i, cell[1]+j))

	if not base:
		ret.remove(cell)

	return ret

def near_group(cells, diagonals=False, base=False):
	ret = set()
	for cell in cells:
		ret = ret.union(near(cell, diagonals=diagonals, base=base))

	if not base:
		ret -= set(cells)

# Переместить обрезку границ в near()
	remove = set()
	for cell in ret:
		for i in cell:
			if not (0 <= i <= size-1):
				remove.add(cell)
				break

	ret -= remove

	return ret

class Field:
	def __init__(self):
		self.field = []
		for i in range(size):
			self.field.append([False]*size)

	def generate(self, ship_count=4):

		for ship_type in range(ship_count):

			for ship_copy in range(ship_count - (ship_type - 1)):

				first_cell = []
				while True:
					for i in range(2):
						first_cell.append(random.randint(0, size-1))

					check = near(first_cell)

					available = True
					for cell in check:
						if self.field[cell[0]][cell[1]] == True:
							available = False
							break

					if available:
						break

				near_cells = near(first_cell)
				for ship_cell in range(ship_type-1):
					new_cell = random.choice(list(near_cells))
					self.field[new_cell[0]][new_cell[1]] = True

	def get_cell(self, coord):
		return self.field[coord[0]][coord[1]]

	def __repr__(self):
		ret = ''

		for i in self.field:
			for j in i:
				ret += ((' ', 'XX')[j])
			ret += ('\n')

		return ret

def make_coord(str_coord):
	if len(str_coord) != 2:
		return None

	str_coord = str_coord.lower()
	ret = (ord(str_coord[0])-97, int(str_coord[1])-1)

	for i in ret:
		if not (0 <= i <= size-1):
			return None

	return ret

if __name__ == '__main__':
	str_coord = input()
	coord = make_coord(str_coord)

	if not coord:
		print('invalid input: first char must be leter A-J, second - digit 1-10')

	f = Field()
	f.generate()
	print(f)
