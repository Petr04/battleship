from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc

from customField import InputField

import validate


class FieldDialog(qw.QDialog):
	def __init__(self, validate, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.f = InputField((10, 10))
		self.validate = validate

		buttons = qw.QDialogButtonBox(
			qw.QDialogButtonBox.Ok | qw.QDialogButtonBox.Cancel,
			qc.Qt.Horizontal, self
		)

		buttons.accepted.connect(self.ok)
		buttons.rejected.connect(self.reject)

		vbox = qw.QVBoxLayout()
		vbox.addWidget(self.f)
		vbox.addWidget(buttons)

		self.setLayout(vbox)


	def field(self):
		return self.f.getField()

	def ok(self):
		if not self.validate:
			self.accept()
		else:

			v = validate.validate(self.field(), {i: 5-i for i in range(1, 5)})

			print(self.field())

			if v:
				self.accept()
			else:
				msg = qw.QMessageBox(self)
				msg.setIcon(qw.QMessageBox.Warning)
				msg.setText('Your field is invalid')
				msg.exec_()

	@staticmethod
	def getField(validate, *args, **kwargs):

		dialog = FieldDialog(validate, *args, **kwargs)

		result = dialog.exec_()
		field = dialog.field()

		return (field, result == qw.QDialog.Accepted)
