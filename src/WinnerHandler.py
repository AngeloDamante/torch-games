"""
A simple class to handle winners. 

Author: Vittorione
Date: December 2024
"""

import csv


# TODO

class WinnerHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_file(self):
        with open(self.file_name, "r") as file:
            reader = csv.DictReader(file, delimiter=";")
            results = [row for row in reader]
        return results
