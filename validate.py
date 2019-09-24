from near import near_group
from split2ships import split2ships

def diagonals(ship):
	return near_group(ship, base=False, diagonals=True) - \
		near_group(ship, base=False, diagonals=False)

def get_count(ships):
	count = {}

	for i in ships:
		l = len(i)

		if l not in count:
			count[l] = 1
		else:
			count[l] += 1

	return count

def check_diagonals(ships):
	for i in ships:
		for j in ships:
			if len( diagonals(i) & j ) != 0:
				return False

	return True

def validate(cells, count):
	ships = split2ships(cells)

	return (count == get_count(ships)) and check_diagonals(ships)

if __name__ == '__main__':
	cells = {(0, 1), (3, 2), (1, 5), (1, 6), (2, 3), (2, 2), (1, 0), (1, 1)}
	ships = split2ships(cells)

	print(check_diagonals(ships))
