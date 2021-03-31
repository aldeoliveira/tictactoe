class Lines:

    def __init__(self, board):
        self.dimension = board.dimension
        self.squares = board.squares
        self.lines = self.get_lines()

    def get_lines(self):
        lines = []
        self.group_rows(lines)
        self.group_columns(lines)
        self.group_diagonals(lines)
        return lines

    def group_rows(self, lines):
        for i in range(self.dimension):
            row = []
            for square in self.squares.values():
                if square.row == i:
                    row.append(square)
            lines.append(row)

    def group_columns(self, lines):
        for j in range(self.dimension):
            column = []
            for square in self.squares.values():
                if square.col == j:
                    column.append(square)
            lines.append(column)

    def group_diagonals(self, lines):
        first_diagonal = []
        for square in self.squares.values():
            if square.row == square.col:
                first_diagonal.append(square)
        lines.append(first_diagonal)
        second_diagonal = []
        for square in self.squares.values():
            if square.row + square.col == self.dimension:
                second_diagonal.append(square)
        lines.append(second_diagonal)
