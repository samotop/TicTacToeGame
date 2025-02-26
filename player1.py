import tkinter as tk


class Player1:
    def __init__(self, name):
        self.is_winner = False
        self.name = name
        self.score = 0

        self.symbol = tk.PhotoImage(file="X.png", width=80, height=80)

        self.status_number = 1

        self.made_turn = False

