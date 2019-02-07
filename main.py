from gameboard import Gameboard
from interface import result
import random

def make_coord(self, str_coord): # a1 -> (0, 0)
	if len(str_coord) != 2:
		return None

	str_coord = str_coord.lower()
	ret = (ord(str_coord[0])-97, int(str_coord[1])-1)

	for i in range(len(ret)):
		if not (0 <= ret[i] <= (self.x, self.y)[i]): # Проверить, нужно ли здесь вычитать 1
													 # или поставить < вместо <=
			return None

	return ret

if __name__ == '__main__':
	players = 2

	comp = Gameboard()
	user = Gameboard()

	comp.generate()
	user.input()

	first = random.randint(players)
	order = ((comp, user)[first], (comp, user)[players-first])

	print('Первым ходит{}'.format((' компьютер', 'е вы')[first]))

	while True:
		for i in range(players):
			if first == 2: # Если ходит пользователь
				str_coord = input('> ')
				x, y = make_coord(str_coord)

				ret = order[i].attack(order[players-i], x, y)
				print(('Мимо', 'Ранил', 'Убил')[ret])
			else:
				order[i].attack(order[players])

				
