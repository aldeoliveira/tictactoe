from tictactoe import Lines


EMPTY = '-'


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

    def check_for_double_threats(self, player_mark):
        empty_squares_in_a_line = 1
        possible_double_threat_squares = self.check_lines(player_mark, empty_squares_in_a_line)

        # Obter número de vezes que cada candidato aparece (valor)
        set_of_possible_double_threat_squares = list(set(possible_double_threat_squares))
        value_of_possible_double_threat_squares = []
        for square in set_of_possible_double_threat_squares:
            value_of_possible_double_threat_squares = (possible_double_threat_squares.count(square))

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