import tkinter as tk
from ui import UI
from menu import MainMenu
from player1 import Player1
from player2 import Player2
from computer import Computer
from square import Square


class App:
    def __init__(self):
        # Initialize main window to keep access for other classes for this atribute
        self.window = None

        #Initialize game modes
        self.player_vs_player = False
        self.player_vs_computer = False

        #Initialize user interface object
        self.user_interface = UI(self)

        #Initialize menu
        self.menu = MainMenu(self)

        self.winner_exists = False

        self.image_x_win = tk.PhotoImage(file="X-win.png", width=80, height=80)
        self.image_letter_o_win = tk.PhotoImage(file="letter-o-win.png", width=80, height=80)

        #Initialize move counter and game counter
        self.move_counter = 0
        self.game_counter = 1
        self.current_player = None

        self.start()

    def set_window(self, window):
        self.window = window

    def start(self):
        self.window.mainloop()

    def create_game_environment(self):
        #Create players
        if self.player_vs_player:
            self.player1 = Player1(self.menu.player1_name.get())
            self.player2 = Player2(self.menu.player2_name.get())

        elif self.player_vs_computer:
            self.player1 = Player1(self.menu.player1_name.get())
            self.player2 = Computer(self)

        #Show up players and score
        self.user_interface.show_players_names()
        self.user_interface.show_players_scores()

        #Set first turn for player 1
        self.current_player = self.player1

        # Show up game field with squares
        self.square = Square(self)
        self.square.squares_setup()

        # Initialize list of lists of win combinations
        self.square.setup_win_combinations()

        #Show move info after game start
        self.user_interface.update_move_text_info()

    def check_for_win_(self):
        for combination in self.square.win_combinations:
            combination_status_sum = combination[0].status + combination[1].status + combination[2].status
            if combination_status_sum == 3:
                self.winner_exists = True
                self.user_interface.show_winner(self.player1.name)

                #Change visual of win combination after win and disable all squares
                for square in combination:
                    square.configure_square_image(image=self.image_x_win)
                self.disable_all_squares()

                #Update game counter
                self.game_counter += 1

                #Update player score and show it on the screen
                self.player1.score += 1
                self.user_interface.player1_score_label.configure(text=f"Score: {self.player1.score}")

                #Show the reset button to reset game field
                self.user_interface.restart_button.place(x=600, y=500)

            elif combination_status_sum == -3:
                self.winner_exists = True
                self.user_interface.show_winner(self.player2.name)

                for square in combination:
                    square.configure_square_image(image=self.image_letter_o_win)
                self.disable_all_squares()

                self.game_counter += 1
                self.player2.score += 1
                self.user_interface.player2_score_label.configure(text=f"Score: {self.player2.score}")

                self.user_interface.restart_button.place(x=600, y=500)

        if self.move_counter == 9 and not self.winner_exists:
            self.game_counter += 1
            self.user_interface.show_draw_info()
            self.winner_exists = True
            self.user_interface.restart_button.place(x=600, y=500)

    def disable_all_squares(self):
        for combination in self.square.win_combinations:
            for square in combination:
                square.is_disabled = True

    def change_turn_after_game(self):
        if self.game_counter % 2 != 0:
            self.current_player = self.player1
        else:
            self.current_player = self.player2

    def reset_score(self):
        self.player1.score = 0
        self.player2.score = 0
        self.user_interface.player1_score_label.configure(text=f"Score: {self.player1.score}")
        self.user_interface.player2_score_label.configure(text=f"Score: {self.player2.score}")

    def switch_turn(self):
        if self.player_vs_computer:
            if self.player1.made_turn:

                self.player1.made_turn = False

                #Computer will make turn after delay
                self.window.after(600, self.player2.make_move)

        else:
            self.current_player = self.player1 if self.current_player == self.player2 else self.player2