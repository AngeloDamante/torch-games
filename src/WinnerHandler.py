"""
A simple class to handle winners. 

Author: Vittorione
CoAuthor: Angelone
Date: December 2024
"""

import os
import csv


class WinnerHandler:
    def __init__(self, file_name):
        self.file_name = file_name
        self.winners = []
        self.headers = ["Name", "Score"]
        self.first_run()
        self.load_winners()

    def first_run(self):
        # check that if csv file exists
        if not os.path.exists(self.file_name):
            with open(self.file_name, mode="w") as file:
                writer = csv.DictWriter(file, fieldnames=self.headers, delimiter=";")
                writer.writeheader()

    def load_winners(self):
        with open(self.file_name, mode="r") as file:
            reader = csv.DictReader(file, delimiter=";")
            self.winners = [row for row in reader]

    def get_winners(self):
        return self.winners

    def add_winner(self, name, score):
        # Update List
        self.winners.append({self.headers[0]: name, self.headers[1]: score})

        # Update File
        with open(self.file_name, mode="a") as f:
            writer = csv.DictWriter(f, fieldnames=self.headers, delimiter=";")
            writer.writerow({self.headers[0]: name, self.headers[1]: score})
