from main import Field

f = Field()

_all = set()
for i in range(9):
	for j in range(9):
		_all.add((i, j))


f.field = {(1, 1), (2, 5)}
print(_all - f.available())
