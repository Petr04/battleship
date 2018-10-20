import random

from near import *
from convert import *

class Field:
	def __init__(self, x=10, y=10):
		self.field = set()

		self.x = x
		self.y = y

		self.all = set()
		for i in range(self.x-1):
			for j in range(self.y-1):
				self.all.add((i, j))

		self.all_busy = 0 # Убрать, когда я переделаю рекурсию в цикл
		self.added = False

	def __repr__(self):
		field = coords_to_field(self.field)
		ret = ''

		for i in field:
			for j in i:
				ret += ((' ', 'X')[j])
			ret += ('\n')

		return ret

	def generate(self, ship_count=4):

		self.all_busy += 1

		for ship_type in range(ship_count):
			ship_type += 1

			for ship_copy in range(ship_count - (ship_type - 1)):

				first = random.choice(list(self.all - near_group(self.field, diagonals=True, base=True))) # Выбирать из доступных
				# для first может не найтись места

				print(first, ship_type)
				print('----------')

				new = {first} # Ячейки нового корабля

				# Я каждый раз генерирую всё поле заново, хотя можно просто
				# попробовать найти другую новую клетку. А если я все перебрал или по
				# другому признаку видно, что уже не найти такой основы, от
				# которой можно было бы сгенерировать корабль, то тогда уже
				# нужно генерировать всё поле заново.

				# Когда нет места, не надо генерировать всё поле заново,
				# можно просто попытаться найти клетку ещё раз. Как это сделать?
				# 1) Надо узнать, есть ли такие клетки, если есть - рандомом
				#    пытаться найти такую, а если нет - генерировать заново
				#    всё поле.
				# 2) Получить список доступных клеток, а если он пуст -
				#    генерировать заново всё поле.

				for ship_cell in range(ship_type-1):
					near = near_group(new)
					print('near: {}'.format(near))

					available = near - near_group(self.field, base=True, diagonals=True)
					if len(available) == 0:
						print('Мы зашли в ступор в {}й раз'.format(self.all_busy))
						self.field = set()
						self.generate()

					new.add(random.choice(list(available)))

				print('Result: {}'.format(new))
				self.field |= new
				print()

	def make_coord(self, str_coord):
		if len(str_coord) != 2:
			return None

		str_coord = str_coord.lower()
		ret = (ord(str_coord[0])-97, int(str_coord[1])-1)

		for i in range(len(ret)):
			if not (0 <= ret[i] <= (self.x, self.y)[i]): # Проверить, нужно ли здесь вычитать 1
				return None

		return ret

if __name__ == '__main__':
	f = Field()

	str_coord = input()
	coord = f.make_coord(str_coord)

	if not coord:
		print('invalid input: first char must be leter A-J, second - digit 1-10')

	f.generate()

	print(f)
