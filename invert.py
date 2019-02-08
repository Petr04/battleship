def invert(field, x=10, y=10):
	ret = set()

	for i in range(x):
		for j in range(y):
			if not ( (i, j) in field ):
				ret.add((i, j))

	return ret

if __name__ == '__main__':
	from gameboard import Gameboard

	f = {(1, 2), (3, 4)}

	p = Gameboard()
	p.field = invert(f)
	print(p)
