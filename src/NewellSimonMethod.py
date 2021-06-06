import random
import copy
from src import LineChecking, SquareChecking, Mark

EMPTY = '-'


class NewellSimonMethod:

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
        """
        Este método seleciona uma casa que não só bloqueia um ataque duplo do oponente, mas também impede que o oponente
        crie um ataque duplo com seu próprio lance. Sua lógica é a seguinte:
         - Ele localiza todas as casas que geram um ataque duplo para o oponente;
         - Se houver apenas uma ameaça de ataque duplo, ocupa essa casa;
         - Se houver mais de uma casa que cria um ataque duplo, deve-se ocupar uma casa que force o oponente a ocupar,
         no próximo lance, uma casa que não gere um ataque duplo.

        A implementação é a seguinte:
            Obter as casas que criam ataques duplos para o oponente,
            Se houver apenas uma ameaça de ataque duplo, ocupar a casa.
            Se houver mais de uma ameaça de ataque duplo,
                Obter todos os lances possíveis,
                Verificar em quais desses lances o oponente é forçado a jogar onde não cria um ataque duplo
        """
        forking_squares = self.line_checking.check_for_forking_squares(self.enemy_mark)
        best_blocking_squares = forking_squares
        if len(forking_squares) > 1:
            squares_that_prevent_all_forks = self.get_squares_that_prevent_all_forks()
            if squares_that_prevent_all_forks:
                best_blocking_squares = squares_that_prevent_all_forks
        return best_blocking_squares

    def get_squares_that_prevent_all_forks(self):
        squares_that_prevent_both_forks = []
        candidates = self.check_for_any_empty_square()
        for square in candidates:
            analysis_gamestate = self.make_a_mark_in_a_analysis_board(square)
            analysis_line_checking = LineChecking.LineChecking(analysis_gamestate.board)
            squares_enemy_has_to_block = analysis_line_checking.check_for_immediate_threats(self.ally_mark)
            if squares_enemy_has_to_block:
                forking_squares_in_analysis_position = analysis_line_checking.check_for_forking_squares(self.enemy_mark)
                same_square = self.check_if_contain_same_squares(forking_squares_in_analysis_position,
                                                                 squares_enemy_has_to_block)
                if not same_square:
                    squares_that_prevent_both_forks.append(square)
        return squares_that_prevent_both_forks

    def make_a_mark_in_a_analysis_board(self, square):
        analysis_gamestate = copy.deepcopy(self.current_gamestate)
        r, c = square.row, square.col
        mark = Mark.Mark((r, c), self.ally_mark)
        analysis_gamestate.change_mark_in_a_square(mark)
        return analysis_gamestate

    def check_if_contain_same_squares(self, first_list, second_list):
        same_squares = []
        for a in first_list:
            for b in second_list:
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
