"""
A simple button ti simulate a torch behaviour. 

Author: Angelone
Date: December 2024
"""

class TorchButton:
    def __init__(self, button):
        self.button = button
        self.reset()

    def reset(self):
        self.button.setStyleSheet("background-color:white;")
        self.is_active = False

    def burn(self) -> bool:
        if self.is_active: return False
        self.is_active = True
        self.button.setStyleSheet("background-color:red;")
        return True

    def trigger(self) -> None:
        self.is_active = not self.is_active
        if self.is_active:
            self.button.setStyleSheet("background-color:red;")
        else:
            self.button.setStyleSheet("background-color:white;")