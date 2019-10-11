from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc

from field import Field
from cellStatus import CellStatus
from result import Result

import numpy as np
from player import Player


result_status = {
	Result.MISS: CellStatus.MISS,
	Result.DAMAGE: CellStatus.DAMAGED,
	Result.KILL: CellStatus.KILLED
}


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
		# damaged и killed должны отображаться на противоположном поле
		l = [
			(self.player.killed, CellStatus.KILLED),
			(self.player.damaged, CellStatus.DAMAGED),
			(self.player.miss, CellStatus.MISS)
		]

		if field:
			l.append((self.player.field, CellStatus.SHIP))

		for t, st in l:
			for i in t:
				self.cells[i[0]][i[1]].setStatus(st)


class EnemyField(GameField):
	clickedSignal = qc.pyqtSignal()

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.clickedCell = None

	def clicked(self):
		self.clickedCell = self.sender()
		self.clickedSignal.emit()


class Gameboard(qw.QWidget):
	def __init__(self, size, myFirst, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.myCurrent = myFirst

		self.me = GameField(size, self)
		self.enemy = EnemyField(size, self)

		self.enemy.player.generate()

		self.enemy.clickedSignal.connect(self.clicked)

		vbox = qw.QVBoxLayout()
		vbox.addWidget(self.me)
		vbox.addWidget(self.enemy)

		self.setLayout(vbox)

		if not self.myCurrent:
			self.move()


	def move(self, c=None):
		myCurrentOld = self.myCurrent
		self.myCurrent = not self.myCurrent

		if myCurrentOld:
			me = self.me
			enemy = self.enemy
		else:
			me = self.enemy
			enemy = self.me

		if not c:
			c = me.player.optimal_cell(enemy.player)

		ret = me.player.attack(enemy.player, c)

		if ret in result_status:
			enemy.cells[c[0]][c[1]].setStatus(result_status[ret])
			if myCurrentOld:
				self.move()
		else:
			if myCurrentOld:
				print('You win')
			else:
				print('Computer wins')

	def clicked(self):
		if self.myCurrent:
			self.move(c=self.sender().clickedCell.coord)
