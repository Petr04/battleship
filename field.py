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

	# Протестировать и исправить повторяющийся код
	def __and__(self, other):
		if (self.x, self.y) != (other.x, other.y):
			raise DifferentSize

		ret = Field(self.x, self.y)

		for i in range(self.x):
			ret.field.append([])
			for j in range(self.y):
				ret.field[i].append(self.field[i] & self.field[j])

		return ret

	def __or__(self, other):
		if (self.x, self.y) != (other.x, other.y):
			raise DifferentSize

		ret = Field(self.x, self.y)

		for i in range(self.x):
			ret.field.append([])
			for j in range(self.y):
				ret.field[i].append(self.field[i] | self.field[j])

		return ret

	def __xor__(self, other):
		if (self.x, self.y) != (other.x, other.y):
			raise DifferentSize

		ret = Field(self.x, self.y)

		for i in range(self.x):
			ret.field.append([])
			for j in range(self.y):
				ret.field[i].append(self.field[i] ^ self.field[j])

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
