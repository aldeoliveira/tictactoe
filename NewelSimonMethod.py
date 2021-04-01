import random
from tictactoe import LineChecking
from tictactoe import SquareChecking

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
    """

    def __init__(self, gamestate):
        self.gamestate = gamestate
        self.best_square = self.find_best_square()

    def find_best_square(self):
        best_square = None
        ally_mark, enemy_mark = self.define_allies_and_enemies()
        board = self.gamestate.board
        line_checking = LineChecking.LineChecking(board)
        square_checking = SquareChecking.SquareChecking()
        best_square = self.check_for_win(best_square, ally_mark, line_checking)
        if not best_square:
            best_square = self.check_for_block(best_square, enemy_mark, line_checking)
        if not best_square:
            best_square = self.check_for_fork(best_square, ally_mark, line_checking)
        if not best_square:
            best_square = self.check_for_fork_block(best_square, enemy_mark, line_checking)
        """
        if not best_square:
            best_square = self.check_for_empty_center(best_square, square_checking)
        if not best_square:
            best_square = self.check_for_opposite_corner(best_square, square_checking)
        if not best_square:
            best_square = self.check_for_empty_corner(best_square, square_checking)
        if not best_square:
            best_square = self.check_for_empty_side(best_square, square_checking)
        """
        if not best_square:
            best_square = self.check_for_any_empty_square(square_checking, board)
        return best_square

    def check_for_win(self, best_square, ally_mark, line_checking):
        immediately_winning_squares = line_checking.check_for_immediate_threats(ally_mark)
        if immediately_winning_squares:
            best_square = self.choose(immediately_winning_squares)
        return best_square

    def check_for_block(self, best_square, enemy_mark, line_checking):
        immediately_losing_squares = line_checking.check_for_immediate_threats(enemy_mark)
        if immediately_losing_squares:
            best_square = self.choose(immediately_losing_squares)
        return best_square

    def check_for_fork(self, best_square, ally_mark, line_checking):
        double_threat_squares = line_checking.check_for_double_threats(ally_mark)
        if double_threat_squares:
            best_square = self.choose(double_threat_squares)
        return best_square

    def check_for_fork_block(self, best_square, enemy_mark, line_checking):
        avoid_double_threat = line_checking.check_for_double_threats(enemy_mark)
        if avoid_double_threat:
            best_square = self.choose(avoid_double_threat)
        return best_square

    def check_for_empty_center(self, best_square):
        empty_center = self.check_if_central_square_is_empty()
        if empty_center:
            best_square = empty_center
        return best_square

    def check_for_opposite_corner(self, best_square):
        opposite_corner = self.check_for_opposite_corner()
        if opposite_corner:
            best_square = self.choose(opposite_corner)
        return best_square

    def check_for_empty_corner(self, best_square):
        empty_corners = self.check_for_empty_corners()
        if empty_corners:
            best_square = self.choose(empty_corners)
        return best_square

    def check_for_empty_side(self, best_square):
        empty_sides = self.check_for_empty_sides()
        if empty_sides:
            best_square = self.choose(empty_sides)
        return best_square

    def check_for_any_empty_square(self, square_checking, board):
        empty_squares = square_checking.get_all_empty_squares(board)
        best_square = self.choose(empty_squares)
        return best_square

    def choose(self, equivalent_moves):
        chosen_move = random.choice(equivalent_moves)
        return chosen_move

    def define_allies_and_enemies(self):
        ally_mark = 'o'
        enemy_mark = 'x'
        if self.gamestate.x_to_play:
            ally_mark = 'x'
            enemy_mark = 'o'
        return ally_mark, enemy_mark
