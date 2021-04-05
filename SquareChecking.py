from tictactoe import Lines
from tictactoe import Reports

EMPTY = '-'


class SquareChecking:

    helper = Reports.Reports()

    def __init__(self, board):
        self.board = board
        self.squares = self.board.squares.values()

    def get_all_empty_squares(self):
        empty_squares = []
        for square in self.squares:
            if square.mark == '-':
                empty_squares.append(square)
        return empty_squares

    def check_if_central_square_is_empty(self):
        central_square_row = central_square_col = 1
        empty_central_square = []
        for square in self.squares:
            if square.row == central_square_row and square.col == central_square_col and square.mark == EMPTY:
                empty_central_square.append(square)
        return empty_central_square

    def get_pairs_of_corners(self):
        lines = Lines.Lines(self.board)
        diagonals = lines.get_diagonals()
        print("diagonals", diagonals)
        corner_squares = []
        central_row = central_col = 1
        for diagonal in diagonals:
            pair_of_corners = []
            for square in diagonal:
                if square.row != central_row and square.col != central_col:
                    pair_of_corners.append(square)
            corner_squares.append(pair_of_corners)
        return corner_squares

    def get_side_squares(self):
        center_row = 1
        center_col = 1
        dimension = self.board.dimension
        side_squares = []
        for square in self.squares:
            if (square.row == center_row and square.col == (dimension - 1 or 0)) \
                    or (square.col == center_col and square.row == (dimension - 1 or 0)):
                side_squares.append(square)
        return side_squares

    def get_opposite_corners(self, player_mark):
        corner_squares = self.get_pairs_of_corners()
        opposite_corners = []
        for pair_of_corners in corner_squares:
            if pair_of_corners[0] == player_mark and pair_of_corners[1] == EMPTY:
                opposite_corners.append(pair_of_corners[1])
            if pair_of_corners[1] == player_mark and pair_of_corners[0] == EMPTY:
                opposite_corners.append(pair_of_corners[0])
        return opposite_corners

    def get_empty_corners(self):
        corner_squares = self.get_pairs_of_corners()
        empty_corners = []
        for pair_of_corners in corner_squares:
            for square in pair_of_corners:
                if square.mark == EMPTY:
                    empty_corners.append(square)
        return empty_corners

    def get_empty_sides(self):
        side_squares = self.get_side_squares()
        empty_sides = []
        for square in side_squares:
            if square.mark == EMPTY:
                empty_sides.append(square)
        return empty_sides

