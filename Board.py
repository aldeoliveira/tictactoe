import Square, Dimensions

EMPTY = Dimensions.EMPTY


class Board:

    def __init__(self, dimension):
        self.dimension = dimension
        self.squares = self.instantiate_squares()

    def instantiate_squares(self):
        squares = {}
        for r in range(self.dimension):
            for c in range(self.dimension):
                square_name = "{}{}".format(r, c)
                square_object = Square.Square(r, c)
                squares[square_name] = square_object
        return squares

    def get_square(self, r, c):
        for square in self.squares.values():
            if square.row == r and square.col == c:
                return square

    def check_if_square_is_empty(self, r, c):
        square = self.get_square(r, c)
        if square.mark == EMPTY:
            return True
        else:
            return False

    def change_mark_in_a_square(self, r, c, symbol):
        square = self.get_square(r, c)
        square.mark = symbol
