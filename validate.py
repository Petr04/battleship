from split2ships import split2ships

from pprint import pprint

def get_count(ships):
	count = {}

	l = len(ships[0])
	s = list( filter(lambda x: len(x) == l, ships) )

	count[l] = len(s)

	if len(s) > 1:
		upd = get_count(list( filter(lambda x: x not in s, ships) ))
		count.update(upd)

	return count

def check_diagonals(ships):
	return True

def validate(cells, count):
	ships = split2ships(cells)

	return (count == get_count(ships)) and check_diagonals(ships)

if __name__ == '__main__':
	cells = {(4, 7), (2, 8), (0, 2), (2, 1), (4, 0), (4, 4), (0, 4),
		(4, 1), (0, 0), (2, 6), (4, 5), (2, 3), (4, 2), (0, 8),
		(2, 7), (4, 6), (0, 6), (2, 0), (0, 9), (2, 4)}

	ships = split2ships(cells)
	pprint(ships)

	print(get_count(list(ships)))
