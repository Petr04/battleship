import sys
from PyQt5 import QtWidgets as qw

from cellStatus import CellStatus
from field import Field
from customField import EnemyField, Gameboard
from fieldDialog import FieldDialog

from player import Player


class MainWindow(qw.QMainWindow):
	def __init__(self):
		super().__init__()

		w = qw.QWidget()

		f, ok = FieldDialog.getField(False, self)

		if not ok:
			sys.exit(0)

		gb = Gameboard((10, 10), self)

		gb.me.player.field = f
		gb.enemy.player.damaged = {(2, 1), (3, 3)}
		gb.me.updateCells(field=True)
		gb.enemy.updateCells(field=False)

		vbox = qw.QVBoxLayout()
		vbox.addWidget(gb)
		w.setLayout(vbox)

		self.setCentralWidget(w)
		self.show()


if __name__ == '__main__':
	app = qw.QApplication(sys.argv)
	w = MainWindow()
	sys.exit(app.exec_())
