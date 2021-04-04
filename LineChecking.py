from tictactoe import Lines
from tictactoe import Reports

EMPTY = '-'
helper = Reports.Reports()


class LineChecking:

    lines = []

    def __init__(self, board):
        self.lines = self.obtain_lines(board)
        self.dimension = board.dimension

    def obtain_lines(self, board):
        lines_object = Lines.Lines(board)
        lines = lines_object.lines
        return lines

    def check_for_immediate_threats(self, player_mark):
        marked_squares_in_a_line = 2
        squares_with_immediate_threat = self.check_lines(player_mark, marked_squares_in_a_line)
        return squares_with_immediate_threat

    def check_for_double_threats(self, player_mark):
        empty_squares_in_a_line = 1
        possible_double_threat_squares = self.check_lines(player_mark, empty_squares_in_a_line)
<<<<<<< HEAD
        helper.print_squares(possible_double_threat_squares)

        double_threat_squares = []
        if possible_double_threat_squares:
            set_of_possible_double_threat_squares = list(set(possible_double_threat_squares))
            helper.print_squares(set_of_possible_double_threat_squares)

            values_of_possible_double_threat_squares = {}
            for square in set_of_possible_double_threat_squares:
                values_of_possible_double_threat_squares[square] = possible_double_threat_squares.count(square)

            max_value = max(values_of_possible_double_threat_squares.values())
            if max_value > 1:
                for square in values_of_possible_double_threat_squares:
                    if values_of_possible_double_threat_squares[square] == max_value:
                        double_threat_squares.append(square)

            helper.print_squares_with_values(values_of_possible_double_threat_squares)
=======
        set_of_possible_double_threat_squares = list(set(possible_double_threat_squares))
        values_of_possible_double_threat_squares = {}
        for square in set_of_possible_double_threat_squares:
            values_of_possible_double_threat_squares[square] = possible_double_threat_squares.count(square)
        max_value = max(values_of_possible_double_threat_squares.values())
        double_threat_squares = []
        for square in values_of_possible_double_threat_squares:
            if values_of_possible_double_threat_squares[square] == max_value:
                double_threat_squares.append(square)
>>>>>>> 1e383e17ed4355b33aa20897e1b420281a2809b8
        return double_threat_squares

    def check_lines(self, player_mark, number_of_marked_squares):
        candidate_squares = []
        number_of_empty_squares = self.dimension - number_of_marked_squares
        for line in self.lines:
            marks_in_the_line = []
            for square in line:
                marks_in_the_line.append(square.mark)
            if marks_in_the_line.count(player_mark) == number_of_marked_squares and \
                    marks_in_the_line.count(EMPTY) == number_of_empty_squares:
                for square in line:
                    if square.mark == EMPTY:
                        candidate_squares.append(square)
        return candidate_squares
