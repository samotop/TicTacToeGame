import random
import tkinter as tk


class Computer:
    def __init__(self, app):
        self.app = app
        self.is_winner = False

        self.name = "Computer"
        self.score = 0
        self.symbol = tk.PhotoImage(file="letter-o.png")
        self.status_number = -1

        self.full_empty_combinations = []
        self.opponent_marked_combinations = []
        self.computer_marked_combinations = []

        self.free_squares_in_computer_marked_combinations = []
        self.free_squares_in_opponent_marked_combinations = []

    def win_move(self):
        for combination in self.app.square.win_combinations:
            combination_status_sum = combination[0].status + combination[1].status + combination[2].status

            # Computer first look for a win move
            if combination_status_sum == -2:
                for square in combination:
                    if square.status == 0:
                        square.configure_square_image(image=self.app.player2.symbol)
                        square.status = self.status_number
                        self.app.move_counter += 1
                        self.app.check_for_win_()
                        self.app.switch_turn()
                        return True
        return False

    def block_opponent_win(self):
        for combination in self.app.square.win_combinations:
            combination_status_sum = combination[0].status + combination[1].status + combination[2].status

            # Second look for destroy opponent win
            if combination_status_sum == 2:
                for square in combination:
                    if square.status == 0:
                        square.configure_square_image(image=self.app.player2.symbol)
                        square.status = self.status_number
                        self.app.move_counter += 1
                        self.app.check_for_win_()
                        self.app.switch_turn()
                        return True
        return False

    # Computer look for a move, with possibility for future win, especially looking for square, which is in 3 complete
    # empty winning combinations

    def strategic_move_3_empty_combinations(self):
        self.find_empty_combinations()
        self.update_empty_comb_existence_number()

        for empty_combination in self.full_empty_combinations:
            for square in empty_combination:
                if square.in_empty_comb_existence_number == 3:
                    square.configure_square_image(image=self.app.player2.symbol)
                    square.status = self.status_number
                    self.app.move_counter += 1
                    self.app.check_for_win_()
                    self.app.switch_turn()
                    return True

        return False

    #Looking for square, which is in 2 complete empty winning combinations
    def strategic_move_2_empty_combinations(self):
        self.find_empty_combinations()
        self.update_empty_comb_existence_number()

        for empty_combination in self.full_empty_combinations:
            for square in empty_combination:
                if square.in_empty_comb_existence_number == 2:
                    square.configure_square_image(image=self.app.player2.symbol)
                    square.status = self.status_number
                    self.app.move_counter += 1
                    self.app.check_for_win_()
                    self.app.switch_turn()
                    return True

        return False

    # Computer look for winning combination, where he has 1 marked square and others are free, but if in this
    # combination is square, which is in another combination where opponent has marked square,
    # computer will mark the square in his combination, which will blok opponent combination

    def strategic_move_1_point_in_combination(self):
        self.free_squares_in_computer_marked_combinations.clear()
        self.free_squares_in_opponent_marked_combinations.clear()

        #Find combinations where opponent has 1 square marked.
        self.find_opponent_marked_combinations()
        #Find all free squares in combinations where opponent has 1 marked square.
        for combination in self.opponent_marked_combinations:
            for square in combination:
                if square.status == 0:
                    self.free_squares_in_opponent_marked_combinations.append(square)

        #Find combinations where computer has 1 square marked.
        self.find_computer_marked_combinations()
        # Find all free squares in combinations where computer has 1 marked square.
        for combination in self.computer_marked_combinations:
            for square in combination:
                if square.status == 0:
                    self.free_squares_in_computer_marked_combinations.append(square)

        for square in self.free_squares_in_computer_marked_combinations:
            if square in self.free_squares_in_opponent_marked_combinations:
                square.configure_square_image(image=self.app.player2.symbol)
                square.status = self.status_number
                self.app.move_counter += 1
                self.app.check_for_win_()
                self.app.switch_turn()
                return True

        return False

    #If nothing what mentioned before, computer will make a random move.
    def random_move(self):
        empty_squares = []
        for combination in self.app.square.win_combinations:
            for square in combination:
                if square.status == 0:
                    empty_squares.append(square)
        try:
            random_square = random.choice(empty_squares)
            random_square.configure_square_image(image=self.app.player2.symbol)
            random_square.status = self.status_number
            self.app.move_counter += 1
            self.app.check_for_win_()
            self.app.switch_turn()
            return

        except IndexError:
            pass

    def find_empty_combinations(self):
        self.full_empty_combinations = []
        for combination in self.app.square.win_combinations:
            combination_status_sum = combination[0].status + combination[1].status + combination[2].status
            if combination_status_sum == 0:
                really_empty_comb_counter = 0
                for square in combination:
                    if square.status == 0:
                        really_empty_comb_counter += 1
                if really_empty_comb_counter == 3:
                    self.full_empty_combinations.append(combination)

    def update_empty_comb_existence_number(self):
        self.app.square.reset_really_empty_comb_counter()

        for combination in self.full_empty_combinations:
            for square in combination:
                square.in_empty_comb_existence_number += 1

    def find_opponent_marked_combinations(self):
        self.opponent_marked_combinations = []

        for combination in self.app.square.win_combinations:
            combination_status_sum = combination[0].status + combination[1].status + combination[2].status
            if combination_status_sum == 1:
                self.opponent_marked_combinations.append(combination)

    def find_computer_marked_combinations(self):
        self.computer_marked_combinations = []

        for combination in self.app.square.win_combinations:
            combination_status_sum = combination[0].status + combination[1].status + combination[2].status
            if combination_status_sum == -1:
                self.computer_marked_combinations.append(combination)

    def make_move(self):
        if not self.win_move():
            if not self.block_opponent_win():
                if not self.strategic_move_3_empty_combinations():
                    if not self.strategic_move_2_empty_combinations():
                        if not self.strategic_move_1_point_in_combination():
                            self.random_move()