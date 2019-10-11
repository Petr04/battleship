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

		# field, myFirst, ok = FieldDialog.getField(False, self)
		field = {(2, 8), (7, 7), (2, 1), (8, 9), (9, 4), (5, 1), (2, 5), (5, 8), (1, 2), (5, 5), (8, 1), (1, 5), (2, 2), (2, 6), (2, 3), (6, 5), (3, 8), (1, 8), (5, 2), (8, 4)}
		myFirst = False
		ok = True

		if not ok:
			sys.exit(0)

		gb = Gameboard((10, 10), myFirst, self)

		gb.me.player.field = field

		vbox = qw.QVBoxLayout()
		vbox.addWidget(gb)
		w.setLayout(vbox)

		self.setCentralWidget(w)
		self.show()


if __name__ == '__main__':
	app = qw.QApplication(sys.argv)
	w = MainWindow()
	sys.exit(app.exec_())
