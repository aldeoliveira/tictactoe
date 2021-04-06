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

    def check_for_forking_squares(self, player_mark):
        possible_forking_squares = self.get_possible_forking_squares(player_mark)
        double_threat_squares = []
        if possible_forking_squares:
            values_of_possible_double_threat_squares = self.evaluate_possible_forking_squares(possible_forking_squares)
            double_threat_squares = self.get_most_dangerous_forking_squares(values_of_possible_double_threat_squares)
        return double_threat_squares

    def get_possible_forking_squares(self, player_mark):
        empty_squares_in_a_line = 1
        possible_double_threat_squares = self.check_lines(player_mark, empty_squares_in_a_line)
        return possible_double_threat_squares

    def evaluate_possible_forking_squares(self, possible_double_threat_squares):
        set_of_possible_double_threat_squares = list(set(possible_double_threat_squares))
        values_of_possible_double_threat_squares = {}
        for square in set_of_possible_double_threat_squares:
            values_of_possible_double_threat_squares[square] = possible_double_threat_squares.count(square)
        return values_of_possible_double_threat_squares

    def get_most_dangerous_forking_squares(self, values_of_possible_double_threat_squares):
        double_threat_squares = []
        max_value = max(values_of_possible_double_threat_squares.values())
        if max_value > 1:
            for square in values_of_possible_double_threat_squares:
                if values_of_possible_double_threat_squares[square] == max_value:
                    double_threat_squares.append(square)
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

    def check_for_win(self, player_mark):
        win = False
        for line in self.lines:
            marks_in_the_line = []
            for square in line:
                marks_in_the_line.append(square.mark)
            if marks_in_the_line.count(player_mark) == self.dimension:
                win = True
        return win
