import tkinter as tk


class Player2:
    def __init__(self, name):
        self.is_winner = False

        self.name = name
        self.score = 0

        self.symbol = tk.PhotoImage(file="letter-o.png")

        self.status_number = -1

