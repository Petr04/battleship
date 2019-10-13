from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc

from customField import GameField, EnemyField
from cellStatus import CellStatus
from result import Result

from player import Player


result_status = {
	Result.MISS: CellStatus.MISS,
	Result.DAMAGE: CellStatus.DAMAGED,
	Result.KILL: CellStatus.KILLED
}


class Gameboard(qw.QWidget):
	win = qc.pyqtSignal()
	lose = qc.pyqtSignal()

	def __init__(self, size, myFirst, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.myCurrent = myFirst
		self.finished = False

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
			(me, enemy) = (self.me, self.enemy)
		else:
			(me, enemy) = (self.enemy, self.me)

		if not c:
			c = me.player.optimal_cell(enemy.player)

		ret = me.player.attack(enemy.player, c)

		if ret in result_status.keys() - [Result.KILL]:
			enemy.cells[c[0]][c[1]].setStatus(result_status[ret])
		else:
			me.updateCells(enemy, False)

			if ret == Result.WIN:
				self.finished = True

				if myCurrentOld:
					self.win.emit()
				else:
					self.lose.emit()

	def clicked(self):
		if self.myCurrent and not self.finished:
			self.move(c=self.sender().clickedCell.coord)
			if not self.finished:
				self.move()
