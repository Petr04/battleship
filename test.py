import gameboard as gb

p1 = gb.Gameboard()
p2 = gb.Gameboard()

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
		if out == 3:
			winner = i
			break

		print(('Мимо', 'Ранил', 'Убил')[out])
		print('killed:', order[i].killed)
		print('target:', order[i].target)
		print('empty:', order[i].empty)

		input()

print('Победил {}'.format(('p1', 'p2')[winner]))
