import tkinter as tk
from tkinter import ttk

COLOR_MAIN = "#50206C"
COLOR_BTN_BLUE = "#0070B3"
COLOR_BG = "#FFE8FF"


class MainMenu:
    def __init__(self, app):
        #Initialize access to App instance
        self.app = app

        # Initialize logo image, logo label and title of the game
        self.image = None
        self.logo = None
        self.title = None

        self.name_logo_setup()
        self.show_title_logo()

        #Initialize main menu frame for menu buttons
        self.main_menu = tk.Frame(self.app.window, width=800, height=600, background=COLOR_BG)
        self.main_menu.place(x=300, y=420)

        #Initialize menu buttons
        self.menu_btn_player_vs_player = None
        self.menu_btn_player_vs_computer = None
        self.menu_btn_quit_game = None

        #Initialize widgets - prompt for player names - player vs player mode
        self.player1_name = None
        self.player1_name_label = None
        self.player2_name = None
        self.player2_name_label = None
        self.save_name_button = None
        self.menu_setup()

    def name_logo_setup(self):
        self.image = tk.PhotoImage(file="tic-tac-toe.png")
        self.logo = tk.Label(self.app.window, image=self.image, background=COLOR_BG)
        self.title = tk.Label(self.app.window, text="Tic Tac Toe", font=("Arial", 40, "bold"),
                              foreground=COLOR_MAIN,
                              background=COLOR_BG)

    def show_title_logo(self):
        self.logo.place(x=270, y=50)
        self.title.place(x=250, y=320)

    def menu_setup(self):
        #Setup parameters for player vs player button
        self.menu_btn_player_vs_player = tk.Button(self.main_menu, text="Player vs. Player",
                                                   command=self.prompt_for_names_player_vs_player_mode,
                                                   font=("Arial", 15, "bold"),
                                                   background=COLOR_BTN_BLUE,
                                                   foreground="white")
        self.menu_btn_player_vs_player.grid(column=0, row=2)

        #Setup parameters for player vs computer button
        self.menu_btn_player_vs_computer = tk.Button(self.main_menu, text="Player vs. Computer",
                                                     command=self.prompt_for_names_player_vs_computer_mode,
                                                     font=("Arial", 15, "bold"),
                                                     background=COLOR_BTN_BLUE,
                                                     foreground="white")
        self.menu_btn_player_vs_computer.grid(column=0, row=3, pady=5)

        #Setup parameters for quit game button
        self.menu_btn_quit_game = tk.Button(self.main_menu, text="Quit Game", command=self.quit_game,
                                            font=("Arial", 15, "bold"),
                                            background="#6B1900",
                                            foreground="white")
        self.menu_btn_quit_game.grid(column=0, row=4)

    def hide_main_menu(self):
        self.main_menu.place_forget()

    def hide_title(self):
        self.title.place_forget()

    def hide_logo(self):
        self.logo.place_forget()

    def prompt_for_names_player_vs_player_mode(self):
        #Hide widgets
        self.hide_main_menu()
        self.hide_title()

        #Activate player vs player mode
        self.app.player_vs_player = True

        #Show entry for player names
        self.player1_name = ttk.Entry(self.app.window, font=("Comic Sans MS", 15, "bold"))
        self.player1_name.place(x=100, y=400)

        self.player1_name_label = ttk.Label(self.app.window, text="Player 1 name:",
                                            font=("Comic Sans MS", 15, "bold"),
                                            background=COLOR_BG)
        self.player1_name_label.place(x=150, y=350)

        self.player2_name = ttk.Entry(self.app.window, font=("Comic Sans MS", 15, "bold"))
        self.player2_name.place(x=450, y=400)

        self.player2_name_label = ttk.Label(self.app.window, text="Player 2 name:",
                                            font=("Comic Sans MS", 15, "bold"),
                                            background=COLOR_BG)
        self.player2_name_label.place(x=500, y=350)

        self.save_name_button = tk.Button(self.app.window, text="Save and play", command=self.prepare_game,
                                          font=("Comic Sans MS", 15, "bold"))
        self.save_name_button.place(x=320, y=500)

    def prompt_for_names_player_vs_computer_mode(self):
        #Hide widgets
        self.hide_main_menu()
        self.hide_title()

        #Activate player vs computer mode
        self.app.player_vs_computer = True

        #Show entry for player name
        self.player1_name = ttk.Entry(self.app.window, font=("Comic Sans MS", 15, "bold"))
        self.player1_name.place(x=280, y=400)

        self.player1_name_label = ttk.Label(self.app.window, text="Player 1 name:",
                                            font=("Comic Sans MS", 15, "bold"),
                                            background=COLOR_BG)
        self.player1_name_label.place(x=330, y=350)

        self.save_name_button = tk.Button(self.app.window, text="Save and play", command=self.prepare_game,
                                          font=("Comic Sans MS", 15, "bold"))
        self.save_name_button.place(x=330, y=500)

    def hide_prompt_player_names(self):
        if self.app.player_vs_player:
            self.player1_name.place_forget()
            self.player1_name_label.place_forget()
            self.player2_name.place_forget()
            self.player2_name_label.place_forget()
            self.save_name_button.place_forget()
        else:
            self.player1_name.place_forget()
            self.player1_name_label.place_forget()
            self.save_name_button.place_forget()

    def prepare_game(self):
        self.hide_title()
        self.hide_logo()

        self.hide_prompt_player_names()
        self.app.create_game_environment()
        self.app.user_interface.back_to_menu.place(x=0, y=500)

    def quit_game(self):
        self.app.window.destroy()
