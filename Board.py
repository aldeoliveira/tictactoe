from tictactoe import Square


class Board:

    number_of_diagonals = 2

    def __init__(self, dimension):
        self.dimension = dimension
        self.squares = self.instanciate_squares()

    def instanciate_squares(self):
        squares = {}
        for r in range(self.dimension):
            for c in range(self.dimension):
                square_name = "{}{}".format(r, c)
                square_object = Square.Square(r, c)
                squares[square_name] = square_object
        return squares
