from tictactoe import Square


class Board:
    """
    Talvez precise criar a classe Lines.
    """
    number_of_rows = None
    number_of_columns = None
    number_of_diagonals = 2
    squares = {}
    rows = []
    columns = []
    diagonals = []

    def __init__(self, dimension):
        self.number_of_rows = self.number_of_columns = dimension
        self.squares = self.instanciate_squares()
        self.rows = self.group_squares_in_rows()
        self.columns = self.group_squares_in_columns()
        self.diagonals = self.group_squares_in_diagonals()

    def instanciate_squares(self):
        squares = {}
        for r in range(self.number_of_rows):
            for c in range(self.number_of_columns):
                square_name = "{}{}".format(r, c)
                square_object = Square.Square(r, c)
                squares[square_name] = square_object
        return squares

    def group_squares_in_rows(self):
        rows = []
        for r in range(self.number_of_rows):
            row = []
            for square in self.squares.values():
                if square.row == r:
                    row.append(square)
            rows.append(row)
        return rows

    def group_squares_in_columns(self):
        columns = []
        for c in range(self.number_of_columns):
            column = []
            for square in self.squares.values():
                if square.col == c:
                    column.append(square)
            columns.append(column)
        return columns

    def group_squares_in_diagonals(self):
        diagonals = [[], []]
        for square in self.squares.values():
            if square.row == square.col:
                diagonals[0].append(square)
            if square.row + square.col == self.number_of_rows - 1:
                diagonals[1].append(square)
        return diagonals
