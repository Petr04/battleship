import numpy as np

class Field:
	def __init__(self, size, elements=set()):
		self.size = size

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

	def __eq__(self, other):
		if self.field == other.field:
			return True

		return False

	def __logic(self, other, operation):
		if self.size != other.size:
			raise ValueError("""a, b in a {} b must have same size, but \
a is {}x{}, b is {}x{}""".format(operation, self.x, self.y, other.x, other.y))

		ret = Field(self.size)

		for i in range(self.size[0]):

			for j in range(self.size[1]):
				ret.field[i][j] = eval('self.field[i][j] {} other.field[i][j]'.format(operation))

		return ret

	def __and__(self, other):
		return self.__logic(other, '&')

	def __or__(self, other):
		return self.__logic(other, '|')

	def __xor__(self, other):
		return self.__logic(other, '^')

	def elements(self):
		ret = set()

		for i in self.field:
			for j in i:
				if j:
					ret.add((i, j))

		return ret

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

f = Field((10, 10), {(1, 1), (1, 2), (3, 4), (4, 4), (4, 3), (0, 6)})
print(f)
print('=====')
print(f.near(base=False, diagonals=True))
