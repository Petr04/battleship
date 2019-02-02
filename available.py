from main import Field

f = Field()

all_ = set()
for i in range(9):
	for j in range(9):
		all_.add((i, j))


f.field = {(1, 1), (2, 5)}
print(all_ - f.available())
