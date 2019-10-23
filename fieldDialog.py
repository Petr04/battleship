import sys
from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc

from customField import InputField

import validate


class FieldDialog(qw.QDialog):
	def __init__(self, validate, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.f = InputField((10, 10))
		self.myFst = qw.QCheckBox('Мой ход первый')

		self.validate = validate

		buttons = qw.QDialogButtonBox(
			qw.QDialogButtonBox.Ok | qw.QDialogButtonBox.Cancel,
			qc.Qt.Horizontal, self
		)

		buttons.accepted.connect(self.ok)
		buttons.rejected.connect(self.reject)

		paramLayout = qw.QVBoxLayout()
		paramLayout.setAlignment(qc.Qt.AlignTop)
		paramLayout.addWidget(self.myFst)

		hbox = qw.QHBoxLayout()
		hbox.addWidget(self.f)
		hbox.addLayout(paramLayout)

		vbox = qw.QVBoxLayout()
		vbox.addLayout(hbox)
		vbox.addWidget(buttons)

		self.setLayout(vbox)


	def field(self):
		return self.f.getField()

	def myFirst(self):
		return self.myFst.isChecked()

	def ok(self):
		if not self.validate:
			self.accept()
		else:

			v = validate.validate(self.field(), {i: 5-i for i in range(1, 5)})

			if v:
				self.accept()
			else:
				msg = qw.QMessageBox(self)
				msg.setIcon(qw.QMessageBox.Warning)
				msg.setText('Поле введено неправильно')
				msg.exec_()

	@staticmethod
	def getField(validate, *args, **kwargs):

		dialog = FieldDialog(validate, *args, **kwargs)

		result = dialog.exec_()
		field = dialog.field()
		myFirst = dialog.myFirst()

		return (field, myFirst, result == qw.QDialog.Accepted)


if __name__ == '__main__':
	app = qw.QApplication(sys.argv)
	w = qw.QWidget()
	print(FieldDialog.getField(False, w)[0])
	w.show()
	sys.exit(app.exec_())
