import sys
from PyQt5 import QtWidgets as qw

from cellStatus import CellStatus
from field import Field
from customField import EnemyField
from gameboard import Gameboard
from fieldDialog import FieldDialog

from player import Player


class MainWindow(qw.QMainWindow):
	def __init__(self):
		super().__init__()

		w = qw.QWidget()

		# field, myFirst, ok = FieldDialog.getField(False, self)
		field = {(2, 8), (7, 7), (2, 1), (8, 9), (9, 4), (5, 1), (2, 5), (5, 8), (1, 2), (5, 5), (8, 1), (1, 5), (2, 2), (2, 6), (2, 3), (6, 5), (3, 8), (1, 8), (5, 2), (8, 4)}
		myFirst = False
		ok = True

		if not ok:
			sys.exit(0)

		gb = Gameboard((10, 10), myFirst, self)
		gb.win.connect(self.win)
		gb.lose.connect(self.lose)

		gb.me.player.field = field
		gb.me.updateCells(gb.enemy, True)

		vbox = qw.QVBoxLayout()
		vbox.addWidget(gb)
		w.setLayout(vbox)

		self.setCentralWidget(w)
		self.show()


	def winLose(self, win):
		msg = qw.QMessageBox(self)
		msg.setIcon(qw.QMessageBox.Information)
		msg.setText('You {}'.format(['lose', 'win'][win]))
		msg.exec_()

	def win(self):
		self.winLose(win=True)

	def lose(self):
		self.winLose(win=False)


if __name__ == '__main__':
	app = qw.QApplication(sys.argv)
	w = MainWindow()
	sys.exit(app.exec_())
