import random
import copy
from tictactoe import LineChecking
from tictactoe import SquareChecking
from tictactoe import Reports
from tictactoe import GameState
from tictactoe import Mark

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
        self.current_gamestate = gamestate
        self.ally_mark, self.enemy_mark = self.define_allies_and_enemies(self.current_gamestate)
        board = self.current_gamestate.board
        self.line_checking = LineChecking.LineChecking(board)
        self.square_checking = SquareChecking.SquareChecking(board)

    def get_best_square(self):
        best_squares = self.check_for_win(self.ally_mark)
        method_used = 1
        if not best_squares:
            best_squares = self.check_for_win(self.enemy_mark)
            method_used = 2
        if not best_squares:
            best_squares = self.check_for_fork(self.ally_mark)
            method_used = 3
        if not best_squares:
            best_squares = self.block_forks()
            method_used = 4
        if not best_squares:
            best_squares = self.check_for_empty_center()
            method_used = 5
        if not best_squares:
            best_squares = self.check_for_opposite_corner(self.enemy_mark)
            method_used = 6
        if not best_squares:
            best_squares = self.check_for_empty_corner()
            method_used = 7
        if not best_squares:
            best_squares = self.check_for_empty_side()
            method_used = 8
        if not best_squares:
            best_squares = self.check_for_any_empty_square()
            method_used = 9
        best_square = self.choose(best_squares)
        print(method_used)
        return best_square

    def check_for_win(self, player_mark):
        immediately_winning_squares = self.line_checking.check_for_immediate_threats(player_mark)
        return immediately_winning_squares

    def check_for_fork(self, player_mark):
        double_threat_squares = self.line_checking.check_for_forking_squares(player_mark)
        return double_threat_squares

    def block_forks(self):
        best_blocking_squares = []
        forking_squares = self.line_checking.check_for_forking_squares(self.enemy_mark)
        if len(forking_squares) > 1:
            candidates = self.check_for_any_empty_square()
            for square in candidates:
                analysis_gamestate = copy.deepcopy(self.current_gamestate)
                r, c = square.row, square.col
                mark = Mark.Mark((r, c), self.ally_mark)
                analysis_gamestate.make_mark(mark)
                analysis_line_checking = LineChecking.LineChecking(analysis_gamestate.board)
                forking_squares_in_analysis_position = analysis_line_checking.check_for_forking_squares(self.enemy_mark)
                square_enemy_has_to_block = analysis_line_checking.check_for_immediate_threats(self.ally_mark)
                same_square = self.check_if_contain_same_squares(forking_squares_in_analysis_position,
                                                                 square_enemy_has_to_block)
                if not same_square:
                    best_blocking_squares.append(same_square)
        return best_blocking_squares

    def check_if_contain_same_squares(self, first_list, second_list):
        same_squares = []
        for a in second_list:
            for b in first_list:
                if a.row == b.row and a.col == b.col:
                    same_squares.append(a)
        return same_squares

    def check_for_empty_center(self):
        empty_center = self.square_checking.check_if_central_square_is_empty()
        return empty_center

    def check_for_opposite_corner(self, player_mark):
        opposite_corner = self.square_checking.get_opposite_corners(player_mark)
        return opposite_corner

    def check_for_empty_corner(self, ):
        empty_corners = self.square_checking.get_empty_corners()
        return empty_corners

    def check_for_empty_side(self):
        empty_sides = self.square_checking.get_empty_sides()
        return empty_sides

    def check_for_any_empty_square(self):
        empty_squares = self.square_checking.get_all_empty_squares()
        return empty_squares

    def choose(self, equivalent_moves):
        if isinstance(equivalent_moves, list):
            chosen_move = random.choice(equivalent_moves)
        else:
            chosen_move = equivalent_moves
        return chosen_move

    def define_allies_and_enemies(self, gamestate):
        ally_mark = 'o'
        enemy_mark = 'x'
        if gamestate.x_to_play:
            ally_mark = 'x'
            enemy_mark = 'o'
        return ally_mark, enemy_mark
