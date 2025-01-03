import sys
from gui.torch_game import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from PySide6.QtGui import QStandardItem, QStandardItemModel
from src.TorchButton import TorchButton
from src.WinnerHandler import WinnerHandler
from datetime import datetime, timedelta


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
        self.winner_timer = QTimer()
        self.start_time = datetime.now()
        self.winner_timer.timeout.connect(lambda: self.ui.timer_visible.setText(str(datetime.now() - self.start_time)))

        # Winners
        # TODO: Read File into ListViewWidget
        self.o_winner_handler = WinnerHandler("data/player_records.csv")
        self.view_model = QStandardItemModel()
        self.ui.list_record.setModel(self.view_model)
        self.view_model.setHorizontalHeaderLabels(["Name", "Score"])
        self.update_view()

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

        # reset winner stopwatch
        self.start_time = datetime.now()

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
            self.winner_timer.start(1)

    def check_status(self):
        self.status_torch[0] = self.button_1.is_active
        self.status_torch[1] = self.button_2.is_active
        self.status_torch[2] = self.button_3.is_active
        self.status_torch[3] = self.button_4.is_active
        self.status_torch[4] = self.button_5.is_active

        if all(self.status_torch):
            self.winner_timer.stop()
            self.status_timer.stop()
            self.ui.btn_reset.setEnabled(False)

            print("YOU WIN!")
            self.o_winner_handler.add_winner(self.ui.name.text(), self.ui.timer_visible.text())
            self.update_view()

    def update_view(self):
        self.view_model.clear()
        winners = self.o_winner_handler.get_winners()
        items = []
        for record in winners:
            items = [QStandardItem(str(record.get(header, ""))) for header in winners[0].keys()]
            self.view_model.appendRow(items)


def main():
    app = QApplication(sys.argv)
    window = CommandTorch()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
