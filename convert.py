def field_to_coords(field):
	ret = set()

	for i in range(len(field)):
		for j in range(len(field[i])):
			if field[i][j] == True:
				ret.add((i, j))

	return ret

def coords_to_field(coords, x=10, y=10):
	ret = []

	for i in range(x):
		ret.append([])
		for j in range(y):
			ret[i].append((i, j) in coords)

	return ret

if __name__ == '__main__':

	def make_field(x, y):
		ret = []
		for i in range(x):
			ret.append([False]*y)

		return ret
	
	field = make_field(10, 10)
	field[5][2] = field[1][7] = field[1][3] = True
	for i in field:
		print(i)

	coords = field_to_coords(field)
	print(coords)

	new_field = coords_to_field(coords, 10, 10)
	for i in new_field:
		print(i)
	print(field == new_field)
