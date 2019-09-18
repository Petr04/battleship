import random

from near import near_group


def member(ship, cell, base, diagonals):
	return len( ship & near_group(set([cell]), base=base, diagonals=diagonals) ) != 0

def merge(ships):
	ret = set()

	for i_ship, ship in enumerate(ships):
		for i in ship:
			new_ship = set()

			for j, s in enumerate(ships):
				if member(s, i, base=True, diagonals=False):
					new_ship |= s

		ret.add(tuple(new_ship))

	return list(map(set, ret))

def split2ships(cells):
	ships = []

	for i in cells:
		index = -1
		for i_ship, ship in enumerate(ships):
			if member(ship, i, base=False, diagonals=False):
				index = i_ship
		
		if index == -1:
			ships.append(set())

		ships[index].add(i)

	return merge(ships)


if __name__ == '__main__':
	cells = [
		(0, 1), (1, 0), (1, 1), (2, 0),
		(2, 3), (3, 3), (3, 2),
		(4, 4), (5, 4), (4, 5),
		(5, 1)
	]

	print(merge([{(3, 2), (2, 3), (3, 3)}, {(0, 1), (2, 0), (1, 0), (1, 1)},
		{(5, 1)}, {(5, 4)}, {(4, 5), (4, 4)}]))

	# random.shuffle(cells)

	# print(cells, '\n')

	# print(split2ships(cells))
