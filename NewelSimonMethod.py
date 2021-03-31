import random
from tictactoe import LineChecking

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
        immediately_winning_square = line_checking.check_for_immediate_threats(ally_mark)
        if immediately_winning_square:
            best_square = self.choose(immediately_winning_square)
        if not best_square:
            immediately_losing_square = line_checking.check_for_immediate_threats(enemy_mark)
            if immediately_losing_square:
                best_square = self.choose(immediately_losing_square)
        """
        if not best_square:
            double_threat_squares = self.check_for_double_threat(ally_mark)
            if double_threat_squares:
                best_square = self.choose(double_threat_squares)
        if not best_square:
            avoid_double_threat = self.check_for_double_threat(enemy_mark)
            if avoid_double_threat:
                best_square = self.choose(avoid_double_threat)
        if not best_square:
            empty_center = self.check_if_central_square_is_empty()
            if empty_center:
                best_square = empty_center
        if not best_square:
            opposite_corner = self.check_for_opposite_corner()
            if opposite_corner:
                best_square = self.choose(opposite_corner)
        if not best_square:
            empty_corners = self.check_for_empty_corners()
            if empty_corners:
                best_square = self.choose(empty_corners)
        if not best_square:
            empty_sides = self.check_for_empty_sides()
            if empty_sides:
                best_square = self.choose(empty_sides)
        """
        if not best_square:
            empty_squares = self.get_all_empty_squares()
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

    def get_all_empty_squares(self):
        empty_squares = []
        board = self.gamestate.board
        squares = board.squares
        for square in squares:
            if square.mark == '-':
                empty_squares.append(square)
        return empty_squares

    """
    def check_if_central_square_is_empty(self):
        central_square = [(1, 1)]
        if self.board[1][1] == EMPTY:
            return central_square
        return False

    def check_for_opposite_corner(self):
        return False

    def check_for_empty_corners(self):
        return False

    def check_for_empty_sides(self):
        return False
    """
