from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc

from field import Field
from cellStatus import CellStatus
from result import Result

import numpy as np
from player import Player


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


class GameField(Field):
	def __init__(self, size, *args, **kwargs):
		super().__init__(size, *args, **kwargs)

		self.player = Player(size)

	def updateCells(self, enemy, field):
		l = [
			(self.player.killed, CellStatus.KILLED),
			(self.player.damaged, CellStatus.DAMAGED),
			(self.player.miss, CellStatus.MISS)
		]

		for t, st in l:
			for i in t:
				enemy.cells[i[0]][i[1]].setStatus(st)

		if field:
			for i in self.player.field:
				self.cells[i[0]][i[1]].setStatus(CellStatus.SHIP)

class EnemyField(GameField):
	clickedSignal = qc.pyqtSignal()

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.clickedCell = None

	def clicked(self):
		self.clickedCell = self.sender()
		self.clickedSignal.emit()
