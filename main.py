import sys
from gui.torch_game import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QColor


class Comand_torch(QMainWindow):
	def __init__(self):
		super(Comand_torch, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# [GUI] torch
		self.ui.Torch_one.clicked.connect(self.click_torch())
		self.ui.Torch_two.clicked.connect(self.click_torch())
		self.ui.Torch_three.clicked.connect(self.click_torch())
		self.ui.Torch_four.clicked.connect(self.click_torch())
		self.ui.Torch_five.clicked.connect(self.click_torch())

	def click_torch(self):
		pass

def main():
	app = QApplication(sys.argv)
	window = Comand_torch()
	window.show()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()