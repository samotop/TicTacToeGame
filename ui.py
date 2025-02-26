import tkinter as tk
from tkinter import ttk

COLOR_BG = "#FFE8FF"


class UI:
    def __init__(self, app):
        self.window = tk.Tk()
        self.window.geometry("800x600")
        self.window.title("Tic Tac Toe")
        self.window["bg"] = COLOR_BG

        #Initialize instance of App class and give self.window
        self.app = app
        self.app.set_window(self.window)

        #Initialize labels for players names
        self.player1_name_label = None
        self.player2_name_label = None

        #Initialize labels for players scores
        self.player1_score_label = None
        self.player2_score_label = None

        #Initialize winner info text label
        self.winner_info_text = ttk.Label(self.window, font=("Comic Sans MS", 20, "bold"), background=COLOR_BG)

        #Initialize draw info text
        self.draw_info = ttk.Label(self.window, text=f"It's a draw!", font=("Comic Sans MS", 20, "bold"),
                                   background=COLOR_BG)
        #Initialize restart button
        self.restart_button = tk.Button(self.window, text="Restart", command=self.restart_game,
                                        font=("Comic Sans MS", 15, "bold"))

        #Initialize back to menu button
        self.back_to_menu = tk.Button(self.window, text="◄ Exit", command=self.back_to_menu,
                                      font=("Comic Sans MS", 15, "bold"))

        #Initialize move text info
        self.move_text = ttk.Label(self.window, font=("Comic Sans MS", 15, "bold"),
                                   background=COLOR_BG)

    def show_players_names(self):
        self.player1_name_label = ttk.Label(self.window, text=self.app.player1.name, font=("Comic Sans MS", 30, "bold"),
                                            background=COLOR_BG)
        self.player1_name_label.place(x=40, y=50)

        self.player2_name_label = ttk.Label(self.window, text=self.app.player2.name, font=("Comic Sans MS", 30, "bold"),
                                            background=COLOR_BG)
        self.player2_name_label.place(x=600, y=50)

    def show_players_scores(self):
        self.player1_score_label = ttk.Label(self.window, text=f"Score: {self.app.player1.score}",
                                             font=("Comic Sans MS", 15, "bold"),
                                             background=COLOR_BG)
        self.player1_score_label.place(x=40, y=100)

        self.player2_score_label = ttk.Label(self.window, text=f"Score: {self.app.player2.score}",
                                             font=("Comic Sans MS", 15, "bold"),
                                             background=COLOR_BG)
        self.player2_score_label.place(x=600, y=100)

    def show_winner(self, winner_name):
        self.move_text.place_forget()
        self.winner_info_text.configure(text=f"{winner_name} is the winner! Congratulations.")
        self.winner_info_text.place(x=150, y=130)

    def show_draw_info(self):
        self.move_text.place_forget()
        self.draw_info.place(x=320, y=130)

    def restart_game(self):
        self.app.winner_exists = False
        self.app.change_turn_after_game()
        self.update_move_text_info()
        self.app.move_counter = 0

        self.restart_button.place_forget()

        #Try to hide draw info if exists
        try:
            self.winner_info_text.place_forget()
        except AttributeError:
            pass
        try:
            self.draw_info.place_forget()
        except AttributeError:
            pass

        #Clear all game squares
        for combination in self.app.square.win_combinations:
            for square in combination:
                square.reset_square()
                square.status = 0

        #If computer is the first to make move in next game, computer will make move after 1sec delay
        if self.app.player_vs_computer:
            if self.app.current_player == self.app.player2:
                self.window.after(1000, self.app.player2.make_move)
                self.app.current_player = self.app.player1

                self.window.after(1400, self.update_move_text_info)

    def update_move_text_info(self):
        if self.app.winner_exists:
            return
        else:
            if self.app.current_player == self.app.player1:
                player_on_move = self.app.player1.name
            else:
                player_on_move = self.app.player2.name

        self.move_text.configure(text=f"{player_on_move}'s move")
        self.move_text.place(x=320, y=130)

    def back_to_menu(self):
        self.restart_game()
        self.app.player_vs_computer = False
        self.app.player_vs_player = False

        self.app.user_interface.move_text.place_forget()
        self.player1_name_label.place_forget()
        self.player2_name_label.place_forget()
        self.player1_score_label.place_forget()
        self.player2_score_label.place_forget()

        self.app.square.hide_squares()

        #Reset score
        self.app.reset_score()

        self.app.menu.show_title_logo()
        self.app.menu.main_menu.place(x=300, y=420)
        self.back_to_menu.place_forget()
