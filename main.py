import sys
from gui.torch_game import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from src.TorchButton import TorchButton


class CommandTorch(QMainWindow):
    def __init__(self):
        super(CommandTorch, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Torch Game")

        # [Buttons]
        self.button_1 = TorchButton(self.ui.Torch_one)
        self.button_2 = TorchButton(self.ui.Torch_two)
        self.button_3 = TorchButton(self.ui.Torch_three)
        self.button_4 = TorchButton(self.ui.Torch_four)
        self.button_5 = TorchButton(self.ui.Torch_five)

        # Disable all buttons
        self.button_1.disable_button()
        self.button_2.disable_button()
        self.button_3.disable_button()
        self.button_4.disable_button()
        self.button_5.disable_button()
        self.ui.btn_reset.setEnabled(False)

        # [GUI] torch
        self.ui.Torch_one.clicked.connect(lambda: self.click_torch_one())
        self.ui.Torch_two.clicked.connect(lambda: self.click_torch_two())
        self.ui.Torch_three.clicked.connect(lambda: self.click_torch_three())
        self.ui.Torch_four.clicked.connect(lambda: self.click_torch_four())
        self.ui.Torch_five.clicked.connect(lambda: self.click_torch_five())

        # [GUI] start and reset
        self.ui.btn_reset.clicked.connect(lambda: self.click_reset())
        self.ui.Start.clicked.connect(lambda: self.click_start())

        # [GUI] Status
        self.status_torch = [False, False, False, False, False]
        self.status_timer = QTimer()
        self.status_timer.timeout.connect(self.check_status)

        # [GUI] Timer 
        # TODO needed timer

    def click_torch_one(self):
        if self.button_1.burn():
            self.button_3.trigger()
            self.button_4.trigger()

    def click_torch_two(self):
        if self.button_2.burn():
            self.button_4.trigger()
            self.button_5.trigger()

    def click_torch_three(self):
        if self.button_3.burn():
            self.button_1.trigger()
            self.button_5.trigger()

    def click_torch_four(self):
        if self.button_4.burn():
            self.button_1.trigger()
            self.button_2.trigger()

    def click_torch_five(self):
        if self.button_5.burn():
            self.button_2.trigger()
            self.button_3.trigger()

    def click_reset(self):
        self.button_1.reset()
        self.button_2.reset()
        self.button_3.reset()
        self.button_4.reset()
        self.button_5.reset()

        # TODO: reset winner timer

    def click_start(self):
        if len(self.ui.name.text()) != 0:
            self.button_1.enable_button()
            self.button_2.enable_button()
            self.button_3.enable_button()
            self.button_4.enable_button()
            self.button_5.enable_button()
            self.click_reset()
            self.ui.btn_reset.setEnabled(True)

            # status timer
            self.status_timer.start(1000)

            # winner timer
            # TODO

    def check_status(self):
        self.status_torch[0] = self.button_1.is_active
        self.status_torch[1] = self.button_2.is_active
        self.status_torch[2] = self.button_3.is_active
        self.status_torch[3] = self.button_4.is_active
        self.status_torch[4] = self.button_5.is_active

        if all(self.status_torch):
            print("YOU WIN!")
            self.status_timer.stop()
            self.ui.btn_reset.setEnabled(False)
            # TODO: aggiornare il file e la lista dei vincitori
            # TODO: reset winner timer
            pass


def main():
    app = QApplication(sys.argv)
    window = CommandTorch()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
