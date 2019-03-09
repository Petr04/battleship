from near import near

class DifferentSize(Exception):
	pass

class Field:
	def __init__(self, x, y, elements={None}):
		self.x = x
		self.y = y

		self.field = []

		for i in range(self.x):
			self.field.append([])

			for j in range(y):
				self.field[i].append((i, j) in elements)

	def __str__(self):
		ret = ''

		for i in self.field:
			for j in i:
				ret += (' ', 'X')[j]
			ret += '\n'

		return ret

	def __eq__(self, other):
		for i in (self.field, other.field), (self.x, other.x), (self,y, other.y):
			if i[0] != i[1]:
				return False

		return True

	def __logic(self, other, operation):
		if (self.x, self.y) != (other.x, other.y):
			raise DifferentSize("""a, b in a {} b must have same size, but \
a is {}x{}, b is {}x{}""".format(operation, self.x, self.y, other.x, other.y))

		ret = Field(self.x, self.y)

		for i in range(self.x):

			for j in range(self.y):
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
		# Не работает
		ret = Field(self.x, self.y)

		for i in range(self.x):
			for j in range(self.y):
				if self.field[i][j]:
					delta = (-1, 0, 1)

					for di in delta:
						for dj in delta:
							if not( (not diagonals) and (not 0 in (i, j)) ):
								if not( (not base) and all(d == 0 for d in (di, dj)) ):
									within = True
									check = zip((i, j), (self.x, self.y))
									for c in check:
										if not( 0 <= c[0] <= c[1] ):
											within = False

									if within:
										ret.field[i][j] = True

		return ret

f = Field(10, 10, {(1, 1), (1, 2), (3, 4), (4, 4), (4, 3), (0, 6)})
print(f)
print('=====')
print(f.near(base=False, diagonals=False))
