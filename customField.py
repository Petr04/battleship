from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc

import numpy as np

from field import Field
from cellStatus import CellStatus


class InputField(Field):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.selected = np.full((self.dim), False)

	def clicked(self):
		c = self.sender().coord
		self.selected[c] = not self.selected[c]

		self.sender().toggle((CellStatus.NORMAL, CellStatus.SHIP))

	def getField(self):
		# Indexes of True
		return set(zip(*map(list, np.where(self.selected))))


class EnemyField(Field):
	def clicked(self):
		cell = self.sender()

		nearCoords = near.near(
			cell.coord,
			diagonals=False,
			base=True
		)

		nearCells = [self.cells[i[0]][i[1]] for i in nearCoords]

		for i in nearCells:
			i.toggle((CellStatus.NORMAL, CellStatus.DAMAGED))
