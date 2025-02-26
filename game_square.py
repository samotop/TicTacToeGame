import tkinter as tk
from tkinter import ttk


class GameSquare:
    def __init__(self, app):
        # Initialize access to App instance
        self.app = app

        #Initialize game squares
        self.image_square = tk.PhotoImage(file="square.png", width=80, height=80)

        # Initialize status for the square
        self.status = 0

        self.square = ttk.Button(self.app.window, image=self.image_square,
                                 command=self.update_square)

        #Set square as disabled - default
        self.is_disabled = False

        self.in_empty_comb_existence_number = 0

    def update_square(self):
        #Check if square is disabled, if yes, square will not update
        if self.is_disabled:
            pass
        else:
            #Add 1 point to move counter
            self.app.move_counter += 1

            #Hide move text info
            self.app.user_interface.move_text.place_forget()
            if self.app.current_player == self.app.player1:
                self.square.configure(image=self.app.player1.symbol)

                #Disable square after move and change square status
                self.is_disabled = True
                self.status = self.app.player1.status_number

                #We need this in player vs computer game
                self.app.player1.made_turn = True

                #Change player turns
                self.app.switch_turn()

                #After time delay show updated move text info
                self.app.user_interface.window.after(300, self.app.user_interface.update_move_text_info)

                # Check for win after move
                self.app.check_for_win_()
            elif self.app.current_player == self.app.player2:
                self.square.configure(image=self.app.player2.symbol)

                #Disable square after move and change square status
                self.is_disabled = True
                self.status = self.app.player2.status_number

                #Change player turns
                self.app.switch_turn()

                # After time delay show updated move text info
                self.app.user_interface.window.after(300, self.app.user_interface.update_move_text_info)

                # Check for win after move
                self.app.check_for_win_()

    def grid(self, **kwargs):
        self.square.grid(**kwargs)

    def place(self, **kwargs):
        self.square.place(**kwargs)

    def configure_square_image(self, image):
        self.square.configure(image=image)

    def reset_square(self):
        self.square.configure(image=self.image_square)
        self.is_disabled = False

    def hide_square(self):
        self.square.place_forget()