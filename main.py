from gameboard import Gameboard
from result import Result

p1 = Gameboard()
p2 = Gameboard()

p1.generate()
p2.generate()

order = (p1, p2)

end = False

while True:
	for i in range(2):
		print('{} ходит'.format(i), end='')


		out = order[i].attack(order[1-i])

		print(out)

		if out == Result.WIN:
			winner = i
			end = True
			break

	if end:
		break

print('Победил {}'.format(('p1', 'p2')[winner]))
