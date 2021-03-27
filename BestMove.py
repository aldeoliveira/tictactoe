import random

EMPTY = '-'


class BestMove:
    """
    Algoritmo de Newel e Simon (1972):
    1) Win
    2) Block
    3) Fork
    4) Prevent fork
    5) Center
    6) Opposite corner
    7) Empty corner
    8) Empty side
    """

    number_of_rows = number_of_cols = 3
    squares_in_a_row = squares_in_a_col = 3
    number_of_diagonals = 2
    squares_in_a_diagonal = 3

    board = []
    rows = []
    cols = []
    diagonals = []
    ally_mark = None
    enemy_mark = None

    def __init__(self, current_gamestate):
        self.board = current_gamestate.board

        self.rows, self.cols, self.diagonals = self.obtain_lines()

        # Verifica quem é o próximo a jogar
        self.ally_mark, self.enemy_mark = self.define_allies_and_enemies(current_gamestate)

        # Criar um vetor de candidatos com todas as casas vazias

        best_moves = self.select_best_moves()
        if best_moves:
            self.chosen_move = self.select_random_move(best_moves)
        else:
            valid_moves = self.get_valid_moves()
            self.chosen_move = self.select_random_move(valid_moves)

    def obtain_lines(self):
        rows = [self.board[0], self.board[1], self.board[2]]
        cols = [[self.board[0][0], self.board[1][0], self.board[2][0]],
                [self.board[0][1], self.board[1][1], self.board[2][1]],
                [self.board[0][2], self.board[1][2], self.board[2][2]]]
        diagonals = [[self.board[0][0], self.board[1][1], self.board[2][2]],
                     [self.board[0][2], self.board[1][1], self.board[2][0]]]
        return rows, cols, diagonals

    def define_allies_and_enemies(self, current_gamestate):
        ally_mark = 'o'
        enemy_mark = 'x'
        if current_gamestate.x_to_play:
            ally_mark = 'x'
            enemy_mark = 'o'
        return ally_mark, enemy_mark

    def get_valid_moves(self):
        valid_moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == '-':
                    valid_moves.append((row, col))
        return valid_moves

    def select_best_moves(self):
        immediate_victories = self.check_for_immediate_threat(self.ally_mark)
        if immediate_victories:
            return immediate_victories
        immediate_threats = self.check_for_immediate_threat(self.enemy_mark)
        if immediate_threats:
            return immediate_threats
        create_double_threat = self.check_for_double_threat(self.ally_mark)
        if create_double_threat:
            return create_double_threat
        avoid_double_threat = self.check_for_double_threat(self.enemy_mark)
        if avoid_double_threat:
            return avoid_double_threat
        empty_center = self.check_if_central_square_is_empty()
        if empty_center:
            return empty_center
        opposite_corner = self.check_for_opposite_corner()
        if opposite_corner:
            return opposite_corner
        empty_corners = self.check_for_empty_corners()
        if empty_corners:
            return empty_corners
        empty_sides = self.check_for_empty_sides()
        if empty_sides:
            return empty_sides
        return False

    def check_for_immediate_threat(self, player_mark):
        empty_squares_in_a_line = 1
        squares_with_immediate_threats = []
        self.check_lines(player_mark, empty_squares_in_a_line, squares_with_immediate_threats)
        return squares_with_immediate_threats

    def check_for_double_threat(self, player_mark):
        empty_squares_in_a_line = 2
        possible_double_threat_squares = []
        # Obter candidatos de todas as fileiras, colunas e diagonais
        self.check_lines(player_mark, empty_squares_in_a_line, possible_double_threat_squares)

        # Obter número de vezes que cada candidato aparece (valor)
        set_of_possible_double_threat_squares = list(set(possible_double_threat_squares))
        value_of_possible_double_threat_squares = []
        for square in set_of_possible_double_threat_squares:
            value_of_possible_double_threat_squares.append(possible_double_threat_squares.count(square))

        # Agrupar cada candidato com seu respectivo valor
        set_of_possible_double_threat_squares_with_values = []
        for index in range(len(set_of_possible_double_threat_squares)):
            set_of_possible_double_threat_squares_with_values.append([set_of_possible_double_threat_squares[index],
                                                                      value_of_possible_double_threat_squares[index]])

        # Finalmente, colocar os candidatos que aparecem o número máximo de vezes num vetor final
        double_threat_squares = []
        if len(value_of_possible_double_threat_squares) != 0:
            max_value = max(value_of_possible_double_threat_squares)
            if max_value > 1:
                for index in range(len(set_of_possible_double_threat_squares_with_values)):
                    if set_of_possible_double_threat_squares_with_values[index][1] == max_value:
                        double_threat_squares.append(set_of_possible_double_threat_squares_with_values[index][0])

        return double_threat_squares

    def check_lines(self, player_mark, empty_squares_in_a_line, list_of_squares):
        self.check_rows(player_mark, empty_squares_in_a_line, list_of_squares)
        self.check_cols(player_mark, empty_squares_in_a_line, list_of_squares)
        self.check_diagonals(player_mark, empty_squares_in_a_line, list_of_squares)

    def check_rows(self, player_mark, empty_squares, list_of_squares):
        marked_squares_in_a_row = self.squares_in_a_row - empty_squares
        for row in range(self.number_of_rows):
            if self.rows[row].count(player_mark) == marked_squares_in_a_row\
                    and self.rows[row].count(EMPTY) == empty_squares:
                for col in range(self.squares_in_a_row):
                    if self.rows[row][col] == EMPTY:
                        list_of_squares.append((row, col))

    def check_cols(self, player_mark, empty_squares, list_of_squares):
        marked_squares_in_a_col = self.squares_in_a_col - empty_squares
        for col in range(self.number_of_cols):
            if self.cols[col].count(player_mark) == marked_squares_in_a_col\
                    and self.cols[col].count(EMPTY) == empty_squares:
                for row in range(self.squares_in_a_col):
                    if self.cols[col][row] == EMPTY:
                        list_of_squares.append((row, col))

    def check_diagonals(self, player_mark, empty_squares, list_of_squares):
        marked_squares = self.squares_in_a_diagonal - empty_squares
        for d in range(self.number_of_diagonals):
            if self.diagonals[d].count(player_mark) == marked_squares\
                    and self.diagonals[d].count(EMPTY) == empty_squares:
                for row in range(self.squares_in_a_diagonal):
                    if self.diagonals[d][row] == EMPTY:
                        col = row
                        if d == 1:
                            col = (self.squares_in_a_diagonal - 1) - row
                        list_of_squares.append((row, col))

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

    def select_random_move(self, best_moves):
        chosen_move = random.choice(best_moves)
        return chosen_move
