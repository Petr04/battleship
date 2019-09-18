def near(cell, diagonals, base, x=10, y=10):
	ret = set()
	delta = (-1, 0, 1)
	for i in delta:
		for j in delta:
			if not((not diagonals) and (not (0 in (i, j)))):
				ret.add((cell[0]+i, cell[1]+j))

	if not base:
		ret.remove(cell)

	remove = set()
	for coord in ret:
		for i in range(len(coord)):
			if not (0 <= coord[i] <= (x, y)[i]-1):
				remove.add(coord)

	ret -= remove

	return ret

def near_group(cells, diagonals, base):
	ret = set()
	for cell in cells:
		ret |= near(cell, diagonals=diagonals, base=base)

	if not base:
		ret -= set(cells)

	return ret
