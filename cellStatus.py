from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import enum

class CellStatus(enum.Enum):
	NORMAL = QColor(Qt.gray)
	SHIP = QColor(Qt.black)
	MISS = QColor(Qt.blue)
	DAMAGED = QColor(Qt.red)
	KILILED = QColor(Qt.darkRed)
