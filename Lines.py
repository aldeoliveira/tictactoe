class Lines:

    def __init__(self, board):
        self.dimension = board.dimension
        self.squares = board.squares
        self.lines = self.get_lines()

    def get_lines(self):
        rows = self.get_rows()
        columns = self.get_columns()
        diagonals = self.get_diagonals()
        lines = rows + columns + diagonals
        return lines

    def get_rows(self):
        rows = []
        for i in range(self.dimension):
            row = []
            for square in self.squares.values():
                if square.row == i:
                    row.append(square)
            rows.append(row)
        return rows

    def get_columns(self):
        columns = []
        for j in range(self.dimension):
            column = []
            for square in self.squares.values():
                if square.col == j:
                    column.append(square)
            columns.append(column)
        return columns

    def get_diagonals(self):
        diagonals = []
        first_diagonal = []
        for square in self.squares.values():
            if square.row == square.col:
                first_diagonal.append(square)
        diagonals.append(first_diagonal)
        second_diagonal = []
        for square in self.squares.values():
            if square.row + square.col == self.dimension - 1:
                second_diagonal.append(square)
        diagonals.append(second_diagonal)
        return diagonals
