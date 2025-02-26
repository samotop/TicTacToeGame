from game_square import GameSquare


class Square:
    def __init__(self, app):
        self.app = app

    def squares_setup(self):
        # First Row Squares
        self.btn_a = GameSquare(self.app)
        self.btn_a.place(x=270, y=200)

        self.btn_b = GameSquare(self.app)
        self.btn_b.place(x=360, y=200)

        self.btn_c = GameSquare(self.app)
        self.btn_c.place(x=450, y=200)

        # Second Row Squares
        self.btn_d = GameSquare(self.app)
        self.btn_d.place(x=270, y=290)

        self.btn_e = GameSquare(self.app)
        self.btn_e.place(x=360, y=290)

        self.btn_f = GameSquare(self.app)
        self.btn_f.place(x=450, y=290)
        # Third Row Squares
        self.btn_g = GameSquare(self.app)
        self.btn_g.place(x=270, y=380)

        self.btn_h = GameSquare(self.app)
        self.btn_h.place(x=360, y=380)

        self.btn_i = GameSquare(self.app)
        self.btn_i.place(x=450, y=380)

    def setup_win_combinations(self):
        self.win_combinations = [
            [self.btn_a, self.btn_b, self.btn_c],
            [self.btn_d, self.btn_e, self.btn_f],
            [self.btn_g, self.btn_h, self.btn_i],
            [self.btn_a, self.btn_d, self.btn_g],
            [self.btn_b, self.btn_e, self.btn_h],
            [self.btn_c, self.btn_f, self.btn_i],
            [self.btn_a, self.btn_e, self.btn_i],
            [self.btn_c, self.btn_e, self.btn_g]
            ]

    def hide_squares(self):
        for combination in self.win_combinations:
            for square in combination:
                square.hide_square()

    def reset_really_empty_comb_counter(self):
        for combination in self.win_combinations:
            for square in combination:
                square.in_empty_comb_existence_number = 0
