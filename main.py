import gameboard as gb
import random

if __name__ == '__main__':
	players = 2

	comp = gb.Gameboard()
	user = gb.Gameboard()

	comp.generate()
	user.input()

	first = random.randint(players)
	order = ((comp, user)[first], (comp, user)[players-first])

	print('Первым ходит{}'.format((' компьютер', 'е вы')[first]))

	while True:
		for i in range(players):
			if first == 2: # Если ходит пользователь
				str_coord = input('> ')
				x, y = gb.make_coord(str_coord)

				ret = order[i].attack(order[players-i], x, y)
				print(('Мимо', 'Ранил', 'Убил')[ret])
			else:
				order[i].attack(order[players])

				
