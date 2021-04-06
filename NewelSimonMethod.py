import random
from tictactoe import LineChecking
from tictactoe import SquareChecking
from tictactoe import Reports

EMPTY = '-'


class NewelSimonMethod:
    """
    Algoritmo de Newel e Simon (1972):
    1) Win
     - Verifica se há uma casa que concede vitória imediata. Se sim, deve ocupá-la.
    2) Block win
     - Verifica se há uma casa que concede vitória imediata ao inimigo. Se sim, deve ocupá-la.
    3) Fork
     - Verifica se há uma casa que permite um ataque duplo. Se sim, deve ocupá-la.
    4) Block fork
     - Verifica se há uma casa que permite ao oponente fazer um ataque duplo. Se sim, deve ocupá-la.
    5) Center
     - Verifica se a casa central está ocupada. Se não, deve ocupá-la.
    6) Opposite corner
     - Verifica se há uma marca inimiga num canto, e se o canto oposto está vazio. Se sim, deve ocupar o canto oposto.
    7) Empty corner
     - Verifica se há um canto vazio. Se sim, deve ocupá-lo.
    8) Empty side
     - Verifica se há um lado vazio. Se sim, deve ocupá-lo.

     Olar!

    """

    helper = Reports.Reports()

    def __init__(self, gamestate):
        self.gamestate = gamestate

    def get_best_square(self):
        ally_mark, enemy_mark = self.define_allies_and_enemies()
        board = self.gamestate.board
        line_checking = LineChecking.LineChecking(board)
        square_checking = SquareChecking.SquareChecking(board)
        best_squares = self.check_for_win(ally_mark, line_checking)
        method_used = 1
        if not best_squares:
            best_squares = self.check_for_win(enemy_mark, line_checking)
            method_used = 2
        if not best_squares:
            best_squares = self.check_for_fork(ally_mark, line_checking)
            method_used = 3
        if not best_squares:
            best_squares = self.check_for_fork(enemy_mark, line_checking)
            method_used = 4
        if not best_squares:
            best_squares = self.check_for_empty_center(square_checking)
            method_used = 5
        if not best_squares:
            best_squares = self.check_for_opposite_corner(enemy_mark, square_checking)
            method_used = 6
        if not best_squares:
            best_squares = self.check_for_empty_corner(square_checking)
            method_used = 7
        if not best_squares:
            best_squares = self.check_for_empty_side(square_checking)
            method_used = 8
        if not best_squares:
            best_squares = self.check_for_any_empty_square(square_checking)
            method_used = 9
        best_square = self.choose(best_squares)
        print(method_used)
        return best_square

    def check_for_win(self, player_mark, line_checking):
        immediately_winning_squares = line_checking.check_for_immediate_threats(player_mark)
        return immediately_winning_squares

    def check_for_fork(self, player_mark, line_checking):
        double_threat_squares = line_checking.check_for_double_threats(player_mark)
        return double_threat_squares

    def check_for_empty_center(self, square_checking):
        empty_center = square_checking.check_if_central_square_is_empty()
        return empty_center

    def check_for_opposite_corner(self, player_mark, square_checking):
        opposite_corner = square_checking.get_opposite_corners(player_mark)
        return opposite_corner

    def check_for_empty_corner(self, square_checking):
        empty_corners = square_checking.get_empty_corners()
        return empty_corners

    def check_for_empty_side(self, square_checking):
        empty_sides = square_checking.get_empty_sides()
        return empty_sides

    def check_for_any_empty_square(self, square_checking):
        empty_squares = square_checking.get_all_empty_squares()
        best_square = None
        if empty_squares:
            best_square = self.choose(empty_squares)
        return best_square

    def choose(self, equivalent_moves):
        if isinstance(equivalent_moves, list):
            chosen_move = random.choice(equivalent_moves)
        else:
            chosen_move = equivalent_moves
        return chosen_move

    def define_allies_and_enemies(self):
        ally_mark = 'o'
        enemy_mark = 'x'
        if self.gamestate.x_to_play:
            ally_mark = 'x'
            enemy_mark = 'o'
        return ally_mark, enemy_mark
