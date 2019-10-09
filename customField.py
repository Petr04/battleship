from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc

from field import Field
from cellStatus import CellStatus

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

	def updateCells(self, field):
		d = {
			self.player.killed: CellStatus.KILLED,
			self.player.damaged: CellStatus.DAMAGED,
			self.player.miss: CellStatus.MISS
		}

		if field:
			d[self.player.field] = CellStatus.SHIP

		for t, st in d:
			for i in t:
				self.cells[i[0]][i[1]].setStatus(st)


class EnemyField(GameField):
	clickedSignal = qc.pyqtSignal()

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.clicked_cell = None

	def clicked(self):
		self.clicked_cell = self.sender()
		self.clickedSignal.emit()


class Gameboard(qw.QWidget):
	def __init__(self, size, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.me = GameField(size, self)
		self.enemy = EnemyField(size, self)

		self.enemy.player.generate()

		self.enemy.clickedSignal.connect(self.clicked)

		vbox = qw.QVBoxLayout()
		vbox.addWidget(self.me)
		vbox.addWidget(self.enemy)

		self.setLayout(vbox)


	def enemyMove(self):
		# self.enemy.player.attack(me)
		pass

	def clicked(self):
		pass
