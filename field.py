from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc

from cellStatus import CellStatus


class Cell(qw.QWidget):
	clicked = qc.pyqtSignal()

	def __init__(self, x, y, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.sideSize = 30
		self.normalColor = qg.QColor(qc.Qt.gray)
		self.selectDiff = (0, 30, -20)
		self.hoverDiff = tuple([20]*3)

		self.status = CellStatus.NORMAL
		self.hovered = False

		self.coord = (x, y)

		self.setMinimumSize(qc.QSize(*[self.sideSize]*2))


	def paintEvent(self, event):
		p = qg.QPainter(self)
		p.setRenderHint(qg.QPainter.Antialiasing)
		
		p.setPen(qc.Qt.transparent)

		brush = self.status.value
		if self.hovered:
			brush = brush.lighter(120)

		p.setBrush(brush)
		p.drawRect(event.rect())


	def setStatus(self, status):
		self.status = status
		self.update()

	def toggle(self, statuses):

		if self.status == statuses[0]:
			self.setStatus(statuses[1])
		elif self.status == statuses[1]:
			self.setStatus(statuses[0])


	def enterEvent(self, event):
		self.hovered = True
		self.update()

	def leaveEvent(self, event):
		self.hovered = False
		self.update()

	def mousePressEvent(self, event):
		self.clicked.emit()


class Field(qw.QWidget):
	def __init__(self, size, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.dim = size
		self.spacing = 4

		grid = qw.QGridLayout(self)
		grid.setSpacing(self.spacing)

		self.cells = []

		for i in range(self.dim[0]):
			row = []
			for j in range(self.dim[1]):
				cell = Cell(i, j)
				cell.clicked.connect(self.clicked)
				row.append(cell)

				grid.addWidget(cell, i, j)

			self.cells.append(row)

		self.setLayout(grid)

	def clicked(self):
		pass
