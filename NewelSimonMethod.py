import random
from tictactoe import LineChecking
from tictactoe import SquareChecking
<<<<<<< HEAD
from tictactoe import Reports
=======
>>>>>>> 1e383e17ed4355b33aa20897e1b420281a2809b8

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

    helper = Reports.Reports()

    def __init__(self, gamestate):
        self.gamestate = gamestate
        self.best_square = self.find_best_square()

    def find_best_square(self):
        ally_mark, enemy_mark = self.define_allies_and_enemies()
        board = self.gamestate.board
        line_checking = LineChecking.LineChecking(board)
<<<<<<< HEAD
        square_checking = SquareChecking.SquareChecking(board)
        """
        
        """
        best_squares = self.check_for_win(ally_mark, line_checking)
        method = "Win"
        if not best_squares:
            best_squares = self.check_for_win(enemy_mark, line_checking)
            method = "Block"
        if not best_squares:
            print("checking forks for ally")
            best_squares = self.check_for_fork(ally_mark, line_checking)
            method = "Fork"
        if not best_squares:
            print("checking forks for enemy")
            best_squares = self.check_for_fork(enemy_mark, line_checking)
            method = "Prevent fork"
        if not best_squares:
            best_squares = self.check_for_empty_center(square_checking)
            method = "Center"
        if not best_squares:
            best_squares = self.check_for_opposite_corner(enemy_mark, square_checking)
            method = "Opposite corner"
        if not best_squares:
            best_squares = self.check_for_empty_corner(square_checking)
            method = "Corner"
        if not best_squares:
            best_squares = self.check_for_empty_side(square_checking)
            method = "Side"
        if not best_squares:
            best_squares = self.check_for_any_empty_square(square_checking)
            method = "Any"
        self.helper.print_squares(best_squares)
        print(method)
        best_square = self.choose(best_squares)
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
=======
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
>>>>>>> 1e383e17ed4355b33aa20897e1b420281a2809b8
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
