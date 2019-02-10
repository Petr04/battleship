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

	def elements(self):
		ret = set()

		for i in self.field:
			for j in i:
				if j:
					ret.add((i, j))

		return ret

f = Field(10, 10, {(1, 1), (2, 2), (3, 3), (3, 4)})
print(f)
