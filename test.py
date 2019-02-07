from gameboard import Gameboard
from interface import Result

p1 = Gameboard()
p2 = Gameboard()

p1.generate()
p2.generate()

print('\n' * 8)

print('p1\n', p1)
print('p2\n', p2)

order = (p1, p2)

while True:
	for i in range(2):
		print('{} ходит'.format(i), end='')


		out = order[i].attack(order[1-i])

		print(out)

		if out == Result.WIN:
			winner = i
			break

		print('killed:', order[i].killed)
		print('damaged:', order[i].damaged)
		print('miss:', order[i].miss)

		input()

print('Победил {}'.format(('p1', 'p2')[winner]))
