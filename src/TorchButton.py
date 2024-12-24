from PySide6.QtWidgets import QPushButton

"""
A simple button ti simulate a torch behaviour. 

Author: Angelone
Date: December 2024
"""

class TorchButton:
    def __init__(self, button):
        self.is_active = False
        self.button = button

    def trigger(self) -> bool:
        self.is_active = not self.is_active
        if self.is_active:
            self.button.setStyleSheet("background-color:red;")
        else:
            self.button.setStyleSheet("background-color:white;")