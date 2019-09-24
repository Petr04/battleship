from near import near_group


def split2ships(cells):
	ships = set()

	for i in cells:
		new = {i}

		add = True
		while add:
			add = False

			for j in cells - new:

				intersection = near_group({j}, base=False, diagonals=False) & new

				if len(intersection) != 0:

					new.add(j)
					add = True

		ships.add(frozenset(new))

	return ships

if __name__ == '__main__':
	cells = {(0, 1), (3, 2), (1, 5), (1, 6), (2, 3), (2, 2), (1, 0), (1, 1)}

	print(split2ships(cells))
