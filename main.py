import sys
from gui.torch_game import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QColor

from src.TorchButton import TorchButton


class CommandTorch(QMainWindow):
	def __init__(self):
		super(CommandTorch, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle("Torch Game")

		# [Buttons]
		self.button_1 = TorchButton(self.ui.Torch_one)
		self.button_3 = TorchButton(self.ui.Torch_three)
		self.button_4 = TorchButton(self.ui.Torch_four)

		# [GUI] torch
		self.ui.Torch_one.clicked.connect(lambda: self.click_torch(1))
		# self.ui.Torch_two.clicked.connect(self.click_torch(2))
		# self.ui.Torch_three.clicked.connect(self.click_torch(3))
		# self.ui.Torch_four.clicked.connect(self.click_torch(4))
		# self.ui.Torch_five.clicked.connect(self.click_torch(5))


	def click_torch(self, torch):
		match torch:
			case 1:
				if self.button_1.burn():
					self.button_3.trigger()
					self.button_4.trigger()
			case 2:
				self.ui.Torch_two.setStyleSheet("background-color:red;")
			case 3:
				self.ui.Torch_three.setStyleSheet("background-color:red;")
			case 4:
				self.ui.Torch_four.setStyleSheet("background-color:red;")
			case 5:
				self.ui.Torch_five.setStyleSheet("background-color:red;")


def main():
	app = QApplication(sys.argv)
	window = CommandTorch()
	window.show()
	sys.exit(app.exec())


if __name__ == '__main__':
	main()