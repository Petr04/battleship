import sys
from PyQt5 import QtWidgets as qw

from cellStatus import CellStatus
from field import Field
from fieldDialog import FieldDialog


class MainWindow(qw.QMainWindow):
	def __init__(self):
		super().__init__()

		w = qw.QWidget()

		f, ok = FieldDialog.getField(self)

		if not ok:
			sys.exit(0)

		field = Field((10, 10), self)
		for i in field.cells:
			for j in i:
				if j.coord in f:
					j.setStatus(CellStatus.SHIP)

		vbox = qw.QVBoxLayout()
		vbox.addWidget(field)

		w.setLayout(vbox)

		self.setCentralWidget(w)
		self.show()


if __name__ == '__main__':
	app = qw.QApplication(sys.argv)
	w = MainWindow()
	sys.exit(app.exec_())
